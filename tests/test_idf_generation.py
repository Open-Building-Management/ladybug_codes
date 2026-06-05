"""Integration tests for IDF generation from YAML geometry"""
import os
import tempfile
import pytest
from pathlib import Path
from honeybee.model import Model
from honeybee.room import Room

# Import the geometry generation script components
# This assumes generate_geometry_from_yaml.py can be imported or executed
from src.idfhub.common import load_config, eval_expr, GEOMETRY, BLOCKS, REPO_ROOT
from src.idfhub.helpers.geometry import complex_room, ApertureManager, add_aperture
from src.idfhub.helpers.matlib import CONSTLIB
from ladybug_geometry.geometry3d import Face3D, Point3D
from honeybee.boundarycondition import Outdoors, Ground
from honeybee.facetype import Wall, Floor, RoofCeiling
from honeybee_energy.writer import model_to_idf


@pytest.fixture
def artifacts_dir():
    """Create a temporary directory for IDF artifacts"""
    tmpdir = Path(tempfile.gettempdir()) / "ladybug_test_artifacts"
    tmpdir.mkdir(exist_ok=True)
    yield tmpdir
    # Don't delete - keep for inspection and artifact collection


class TestIDFGenerationFromYAML:
    """Test IDF file generation from YAML geometry configuration"""

    def test_generate_idf_from_agence_yaml(self, artifacts_dir):
        """Test generating IDF from the default agence.yml configuration"""
        geometry = GEOMETRY
        assert geometry is not None, "GEOMETRY not loaded"
        assert "blocks" in geometry, "No blocks in GEOMETRY"

        # Build rooms from YAML
        site = {}
        buildings = []

        common_height = geometry.get("height", 3)

        def prepare(coordinates, variables=None):
            """Prepare coordinates, evaluating formulas if needed"""
            if variables is None:
                return [Point3D(*row) for row in coordinates]
            return [
                Point3D(*[
                    eval_expr(el, variables) if isinstance(el, str) else el
                    for el in row
                ])
                for row in coordinates
            ]

        def get_variables(metadata):
            """Extract variables from level metadata"""
            variables = {}
            variables["height"] = metadata.get("height", common_height)
            variables["altitude"] = metadata.get("altitude", 0)
            return variables

        # Generate rooms
        for building_name, building_metadata in geometry.items():
            if not isinstance(building_metadata, dict) or "blocks" in building_name:
                continue

            building = []
            building_dict = {}

            for level_name, level_metadata in building_metadata.items():
                if not isinstance(level_metadata, dict) or "walls" not in level_metadata:
                    continue

                level_variables = get_variables(level_metadata)
                wall_points = []

                for x in level_metadata["walls"]:
                    if isinstance(x, str) and x in BLOCKS:
                        wall_points.extend(BLOCKS[x])
                    elif isinstance(x, list):
                        wall_points.append(x)

                walls = prepare(wall_points, variables=level_variables)
                
                # Build room
                floors = []
                if "floors" in level_metadata:
                    for x in level_metadata["floors"]:
                        if isinstance(x, str) and x in BLOCKS:
                            floors.append(prepare(BLOCKS[x]))

                level = complex_room(
                    walls,
                    height=level_variables["height"],
                    identifier=level_name,
                    floors=floors if floors else None,
                    use_polyface=not floors
                )
                building.append(level)
                building_dict[level_name] = level

            if building:
                site[building_name] = building_dict
                buildings.extend(building)

        # Create model
        model_name = geometry.get("name", "AgenceACF")
        model = Model(model_name, buildings)
        Room.solve_adjacency(model.rooms)

        # Apply constructions
        for building_name, building_metadata in geometry.items():
            if not isinstance(building_metadata, dict) or "blocks" in building_name:
                continue

            for level_name, level_metadata in building_metadata.items():
                if (not isinstance(level_metadata, dict) or 
                    "walls" not in level_metadata or
                    building_name not in site or
                    level_name not in site[building_name]):
                    continue

                constructions = level_metadata.get("constructions", {})
                room = site[building_name][level_name]

                for face in room.faces:
                    if isinstance(face.type, Wall):
                        construction = constructions.get("walls", "wall_parpaing")
                        if construction in CONSTLIB:
                            face.properties.energy.construction = CONSTLIB[construction]
                    elif isinstance(face.type, Floor):
                        construction = constructions.get("floors")
                        if construction and construction in CONSTLIB:
                            if face.boundary_condition != Ground():
                                face.properties.energy.construction = CONSTLIB[construction]
                    elif isinstance(face.type, RoofCeiling):
                        construction = constructions.get("roofs")
                        if construction and construction in CONSTLIB:
                            if face.boundary_condition != Outdoors():
                                face.properties.energy.construction = CONSTLIB[construction]

        # Generate IDF file
        idf_path = artifacts_dir / f"{model_name}.idf"
        idf_content = model_to_idf(model)
        
        with open(idf_path, "w", encoding="utf-8") as f:
            f.write(idf_content)

        # Verify IDF was created and has content
        assert idf_path.exists(), f"IDF file not created at {idf_path}"
        assert idf_path.stat().st_size > 0, "IDF file is empty"
        
        # Verify IDF content has expected sections
        idf_text = idf_path.read_text()
        assert "Building" in idf_text, "IDF missing Building section"
        assert "Room" in idf_text or "Zone" in idf_text, "IDF missing Room/Zone section"
        
        print(f"\n✅ Generated IDF: {idf_path}")
        print(f"   Size: {idf_path.stat().st_size} bytes")
        print(f"   Rooms: {len(model.rooms)}")

    def test_generate_minimal_idf(self, artifacts_dir):
        """Test generating a minimal IDF from scratch"""
        # Create a simple rectangular room
        wall_points = [
            Point3D(0, 0, 0),
            Point3D(10, 0, 0),
            Point3D(10, 10, 0),
            Point3D(0, 10, 0),
        ]

        room = complex_room(
            wall_points,
            height=3,
            identifier="SimpleRoom",
        )

        # Create model
        model = Model("MinimalBuilding", [room])
        
        # Apply default construction
        for face in room.faces:
            if isinstance(face.type, Wall):
                face.properties.energy.construction = CONSTLIB["wall_osb"]

        # Generate IDF
        idf_path = artifacts_dir / "minimal_building.idf"
        idf_content = model_to_idf(model)
        
        with open(idf_path, "w", encoding="utf-8") as f:
            f.write(idf_content)

        assert idf_path.exists()
        assert idf_path.stat().st_size > 0
        print(f"\n✅ Generated minimal IDF: {idf_path}")

    def test_generate_idf_with_apertures(self, artifacts_dir):
        """Test IDF generation with apertures and doors"""
        # Create a room with apertures
        wall_points = [
            Point3D(0, 0, 0),
            Point3D(10, 0, 0),
            Point3D(10, 5, 0),
            Point3D(0, 5, 0),
        ]

        room = complex_room(
            wall_points,
            height=3,
            identifier="RoomWithApertures",
        )

        # Add apertures to the first wall
        walls = [f for f in room.faces if isinstance(f.type, Wall)]
        if walls:
            wall = walls[0]
            
            # Create a window aperture
            window_points = [
                Point3D(2, 0, 0.9),
                Point3D(3, 0, 0.9),
                Point3D(3, 0, 2.2),
                Point3D(2, 0, 2.2),
            ]
            
            add_aperture(
                wall,
                Face3D(window_points),
                construction=CONSTLIB["window_pvc"],
                label="window_1",
                aperture_type="aperture"
            )
            
            # Create a door aperture
            door_points = [
                Point3D(5, 0, 0),
                Point3D(6.5, 0, 0),
                Point3D(6.5, 0, 2.1),
                Point3D(5, 0, 2.1),
            ]
            
            wall.boundary_condition = Outdoors()
            add_aperture(
                wall,
                Face3D(door_points),
                construction=CONSTLIB["simple_glass_wall"],
                label="door_1",
                aperture_type="door"
            )

        # Create model
        model = Model("BuildingWithApertures", [room])
        
        # Apply constructions
        for face in room.faces:
            if isinstance(face.type, Wall):
                face.properties.energy.construction = CONSTLIB["wall_osb"]

        # Generate IDF
        idf_path = artifacts_dir / "building_with_apertures.idf"
        idf_content = model_to_idf(model)
        
        with open(idf_path, "w", encoding="utf-8") as f:
            f.write(idf_content)

        assert idf_path.exists()
        assert idf_path.stat().st_size > 0
        
        # Verify apertures in IDF
        idf_text = idf_path.read_text()
        assert "FenestrationSurface" in idf_text or "Window" in idf_text, "IDF missing window"
        
        print(f"\n✅ Generated IDF with apertures: {idf_path}")
        print(f"   Windows: {len([f for f in room.apertures])}")
        print(f"   Doors: {len([f for f in room.doors])}")

    def test_generate_multi_room_idf(self, artifacts_dir):
        """Test IDF generation with multiple rooms and floors"""
        # Create two rooms
        room1_points = [
            Point3D(0, 0, 0),
            Point3D(10, 0, 0),
            Point3D(10, 10, 0),
            Point3D(0, 10, 0),
        ]
        room1 = complex_room(room1_points, height=3, identifier="GroundFloor")

        room2_points = [
            Point3D(0, 0, 3),
            Point3D(10, 0, 3),
            Point3D(10, 10, 3),
            Point3D(0, 10, 3),
        ]
        room2 = complex_room(room2_points, height=3, identifier="FirstFloor")

        # Create model with multiple rooms
        model = Model("MultiStoryBuilding", [room1, room2])
        Room.solve_adjacency(model.rooms)

        # Apply constructions
        for room in model.rooms:
            for face in room.faces:
                if isinstance(face.type, Wall):
                    face.properties.energy.construction = CONSTLIB["wall_osb"]
                elif isinstance(face.type, Floor):
                    face.properties.energy.construction = CONSTLIB["floor_internal"]

        # Generate IDF
        idf_path = artifacts_dir / "multi_story_building.idf"
        idf_content = model_to_idf(model)
        
        with open(idf_path, "w", encoding="utf-8") as f:
            f.write(idf_content)

        assert idf_path.exists()
        assert idf_path.stat().st_size > 0
        assert len(model.rooms) == 2
        
        print(f"\n✅ Generated multi-room IDF: {idf_path}")
        print(f"   Rooms: {len(model.rooms)}")


class TestIDFArtifactGeneration:
    """Test that IDFs are ready for GitHub Actions artifact collection"""

    def test_idf_files_are_readable(self, artifacts_dir):
        """Verify all generated IDF files are valid text"""
        idf_files = list(artifacts_dir.glob("*.idf"))
        
        for idf_path in idf_files:
            # Verify file is readable UTF-8
            try:
                content = idf_path.read_text(encoding="utf-8")
                assert len(content) > 100, f"IDF file too small: {idf_path}"
            except UnicodeDecodeError:
                pytest.fail(f"IDF file is not valid UTF-8: {idf_path}")

    def test_idf_summary_generation(self, artifacts_dir):
        """Generate a summary document of all produced IDFs"""
        idf_files = list(artifacts_dir.glob("*.idf"))
        
        summary_path = artifacts_dir / "IDF_SUMMARY.md"
        
        with open(summary_path, "w") as f:
            f.write("# Generated IDF Files\n\n")
            f.write(f"Generated at: {Path(artifacts_dir).resolve()}\n\n")
            
            for idf_path in sorted(idf_files):
                size_kb = idf_path.stat().st_size / 1024
                f.write(f"## {idf_path.name}\n")
                f.write(f"- **Size:** {size_kb:.1f} KB\n")
                f.write(f"- **Path:** `{idf_path}`\n")
        
        print(f"\n📋 Generated summary: {summary_path}")
        print(summary_path.read_text())

    def test_idf_directory_info(self, artifacts_dir):
        """Print directory information for GitHub Actions"""
        idf_files = list(artifacts_dir.glob("*.idf"))
        total_size = sum(f.stat().st_size for f in idf_files)
        
        print("\n" + "="*60)
        print("📦 IDF Artifacts Summary")
        print("="*60)
        print(f"Location: {artifacts_dir}")
        print(f"Total Files: {len(idf_files)}")
        print(f"Total Size: {total_size / 1024:.1f} KB")
        print("="*60)
        
        for idf_path in sorted(idf_files):
            size_kb = idf_path.stat().st_size / 1024
            print(f"  ✅ {idf_path.name:<35} {size_kb:>8.1f} KB")
        print("="*60)
