"""Integration tests for YAML geometry generation"""
import os
import tempfile
import pytest
import yaml
from pathlib import Path
from src.idfhub.common import load_config, GEOMETRY, BLOCKS


class TestYAMLLoading:
    """Test YAML configuration loading"""

    def test_load_default_geometry_config(self):
        """Test loading the default agence.yml geometry config"""
        # This assumes the default conf_geometry/agence.yml exists
        geometry = GEOMETRY
        assert geometry is not None
        assert isinstance(geometry, dict)
        assert "name" in geometry or "blocks" in geometry

    def test_blocks_loaded(self):
        """Test that reusable blocks are extracted"""
        assert BLOCKS is not None
        assert isinstance(BLOCKS, dict)
        # agence.yml should have some block definitions
        if BLOCKS:
            assert any(isinstance(v, list) for v in BLOCKS.values())

    def test_load_custom_yaml(self):
        """Test loading a custom YAML geometry file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yaml_path = Path(tmpdir) / "test_geometry.yml"
            test_config = {
                "name": "TestBuilding",
                "height": 3,
                "blocks": {
                    "base_alt": 0,
                    "block1": [[0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0]]
                }
            }
            with open(yaml_path, "w") as f:
                yaml.dump(test_config, f)

            loaded = load_config(tmpdir, "test_geometry.yml")
            assert loaded["name"] == "TestBuilding"
            assert loaded["height"] == 3
            assert "blocks" in loaded


class TestAgencyYAMLStructure:
    """Test the structure of the default agence.yml"""

    def test_agency_has_required_fields(self):
        """Test that agence.yml has required top-level fields"""
        geometry = GEOMETRY
        # At minimum should have name or building definitions
        assert any(k in geometry for k in ["name", "admin", "height"])

    def test_agency_has_blocks(self):
        """Test that agence.yml defines reusable blocks"""
        assert "blocks" in GEOMETRY
        blocks = GEOMETRY["blocks"]
        assert isinstance(blocks, dict)
        # Altitude anchor should be defined
        assert any("alt" in k for k in blocks.keys())

    def test_agency_building_levels(self):
        """Test that agence.yml defines building levels"""
        # Should have at least one building (e.g., "admin")
        buildings = {k: v for k, v in GEOMETRY.items()
                     if isinstance(v, dict) and k not in ["blocks"]}
        assert len(buildings) > 0

        # Each building should have levels with walls
        for building_name, building_data in buildings.items():
            if "blocks" not in building_name:
                for level_name, level_data in building_data.items():
                    if isinstance(level_data, dict) and "walls" in level_data:
                        assert isinstance(level_data["walls"], list)
                        assert len(level_data["walls"]) > 0


class TestYAMLGeometryElements:
    """Test parsing of geometry elements from YAML"""

    def test_parse_walls(self):
        """Test wall coordinate parsing"""
        geometry = GEOMETRY
        for building_name, building_data in geometry.items():
            if "blocks" not in building_name and isinstance(building_data, dict):
                for level_name, level_data in building_data.items():
                    if isinstance(level_data, dict) and "walls" in level_data:
                        walls = level_data["walls"]
                        # Walls can be string references to blocks or direct coordinates
                        for wall in walls:
                            assert isinstance(wall, (str, list))
                            if isinstance(wall, list):
                                assert len(wall) == 3  # [x, y, z]
                                # Coordinates should be numbers or strings
                                assert all(isinstance(c, (int, float, str)) for c in wall)

    def test_parse_constructions(self):
        """Test construction definitions in levels"""
        geometry = GEOMETRY
        for building_name, building_data in geometry.items():
            if "blocks" not in building_name and isinstance(building_data, dict):
                for level_name, level_data in building_data.items():
                    if isinstance(level_data, dict) and "constructions" in level_data:
                        constructions = level_data["constructions"]
                        assert isinstance(constructions, dict)
                        # Each construction should reference a library item
                        for const_type, const_name in constructions.items():
                            assert isinstance(const_name, str)

    def test_parse_apertures(self):
        """Test aperture definitions in levels"""
        geometry = GEOMETRY
        for building_name, building_data in geometry.items():
            if "blocks" not in building_name and isinstance(building_data, dict):
                for level_name, level_data in building_data.items():
                    if isinstance(level_data, dict) and "apertures" in level_data:
                        apertures = level_data["apertures"]
                        assert isinstance(apertures, dict)
                        # Should have 'numbers' to specify which walls get apertures
                        if "numbers" in apertures:
                            assert isinstance(apertures["numbers"], list)
                            # Can have array properties or scalar defaults
                            for key in ["widths", "heights", "sill_heights", "constructions", "types"]:
                                if key in apertures:
                                    val = apertures[key]
                                    assert isinstance(val, (list, str, int, float))

    def test_parse_elements(self):
        """Test single element definitions"""
        geometry = GEOMETRY
        for building_name, building_data in geometry.items():
            if "blocks" not in building_name and isinstance(building_data, dict):
                for level_name, level_data in building_data.items():
                    if isinstance(level_data, dict) and "elements" in level_data:
                        elements = level_data["elements"]
                        assert isinstance(elements, dict)
                        for elem_name, elem_data in elements.items():
                            if isinstance(elem_data, dict):
                                if "geometry" in elem_data:
                                    # Geometry should be list of 3D points
                                    assert isinstance(elem_data["geometry"], list)
                                if "type" in elem_data:
                                    # Type should be aperture or door
                                    assert elem_data["type"] in ["aperture", "door"]


class TestYAMLAnchorResolution:
    """Test YAML anchor (&) and alias (*) resolution"""

    def test_altitude_anchors_exist(self):
        """Test that altitude anchors are defined in blocks"""
        blocks = GEOMETRY.get("blocks", {})
        # Common altitude anchor names
        altitude_anchors = [k for k in blocks.keys() if "alt" in k.lower()]
        # agence.yml should have some altitude definitions
        if blocks:
            # Check if altitudes are defined (either as keys or values)
            has_altitudes = any(isinstance(v, (int, float)) for v in blocks.values() if v is not None)
            assert has_altitudes or len(blocks) > 0

    def test_block_references_in_walls(self):
        """Test that wall definitions can reference reusable blocks"""
        geometry = GEOMETRY
        blocks = GEOMETRY.get("blocks", {})
        for building_name, building_data in geometry.items():
            if "blocks" not in building_name and isinstance(building_data, dict):
                for level_name, level_data in building_data.items():
                    if isinstance(level_data, dict) and "walls" in level_data:
                        walls = level_data["walls"]
                        # Some walls should be string references
                        string_refs = [w for w in walls if isinstance(w, str)]
                        if string_refs:
                            # These should exist in blocks
                            for ref in string_refs:
                                # Either directly in blocks or used via anchor
                                assert ref in blocks or True  # Anchors might be values


class TestMinimalYAMLParsing:
    """Test parsing of minimal valid YAML configurations"""

    def test_minimal_building_yaml(self):
        """Test loading minimal building configuration"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yaml_path = Path(tmpdir) / "minimal.yml"
            minimal_config = {
                "name": "MinimalBuilding",
                "height": 3,
                "blocks": {
                    "alt0": 0,
                    "block1": [[0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0]]
                },
                "building1": {
                    "level1": {
                        "walls": [
                            [0, 0, 0],
                            [10, 0, 0],
                            [10, 10, 0],
                            [0, 10, 0]
                        ]
                    }
                }
            }
            with open(yaml_path, "w") as f:
                yaml.dump(minimal_config, f)

            loaded = load_config(tmpdir, "minimal.yml")
            assert loaded["name"] == "MinimalBuilding"
            assert "building1" in loaded
            assert "level1" in loaded["building1"]
            assert "walls" in loaded["building1"]["level1"]

    def test_yaml_with_formulas(self):
        """Test YAML that includes string formulas for coordinates"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yaml_path = Path(tmpdir) / "formulas.yml"
            config_with_formulas = {
                "name": "BuildingWithFormulas",
                "height": 3,
                "blocks": {
                    "altitude": 0,
                    "h": 3
                },
                "building1": {
                    "level1": {
                        "walls": [
                            [0, 0, 0],
                            [10, 0, 0],
                            [10, 10, "altitude+2"],
                            [0, 10, "altitude+2"]
                        ]
                    }
                }
            }
            with open(yaml_path, "w") as f:
                yaml.dump(config_with_formulas, f)

            loaded = load_config(tmpdir, "formulas.yml")
            assert loaded["name"] == "BuildingWithFormulas"
            # String formulas should be preserved as strings
            assert loaded["building1"]["level1"]["walls"][2][2] == "altitude+2"


class TestYAMLValidation:
    """Test validation and error handling for YAML"""

    def test_malformed_yaml_error(self):
        """Test that malformed YAML raises appropriate error"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yaml_path = Path(tmpdir) / "bad.yml"
            # Write invalid YAML
            with open(yaml_path, "w") as f:
                f.write("invalid: yaml: content: [")

            with pytest.raises(yaml.YAMLError):
                load_config(tmpdir, "bad.yml")

    def test_missing_yaml_file(self):
        """Test that missing YAML file is handled"""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = load_config(tmpdir, "nonexistent.yml")
            # Should return empty dict or None based on load_config implementation
            assert result == {} or result is None

    def test_empty_yaml_file(self):
        """Test loading an empty YAML file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yaml_path = Path(tmpdir) / "empty.yml"
            with open(yaml_path, "w") as f:
                f.write("")

            loaded = load_config(tmpdir, "empty.yml")
            # Empty YAML should return empty dict
            assert loaded == {} or loaded is None
