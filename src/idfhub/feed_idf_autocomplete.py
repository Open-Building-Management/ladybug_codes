"""generate helpers to autocomplete EP classes and objects"""
from __future__ import annotations
from pathlib import Path
import re
import argparse
from eppy.modeleditor import IDF

from idfhub.helpers.consts import REPO_ROOT

# ---------------- CONFIG ----------------
OS_EP_PATH = "C:/openstudioapplication-1.8.0/EnergyPlus"
IDF_PATH = f"{REPO_ROOT}/empty.idf"
TYPES_NAME = "idf_types_short"
HELPERS_NAME = "idf_helpers_short"
# no more than 50 variables like Field_1, Field_2, etc etc
BREAKOUT_PATTERN: str|None = "_50"
MANUAL = False

types_lines = [
    "from __future__ import annotations",
    "from typing import TypedDict, Literal",
    "",
]

helpers_lines = [
    "from __future__ import annotations",
    f"from .{TYPES_NAME} import *",
    "",
]
# ----------------------------------------

def clean_name(name: str) -> str:
    """Convert EnergyPlus names to valid Python identifiers."""
    name = name.strip().replace(" ", "_").replace("-", "_").replace(".", "")
    name = re.sub(r"[^0-9a-zA-Z_]", "", name)
    if name and name[0].isdigit():
        name = "_" + name
    return name

def py_class_name(objname: str) -> str:
    """Convert EnergyPlus class name to Python class name."""
    return "".join(p.capitalize() for p in objname.replace("-", "").replace(":", " ").split())

def manual():
    """manual exploration"""
    idf = IDF(IDF_PATH)
    all_classes = idf.idfobjects
    for c in sorted(all_classes):
        print(c)
        input("press a key")
        dummy = idf.newidfobject(c)
        for attr in dummy.fieldnames:
            print(attr)
        input("press a key")

def append(idf, c):
    """append to types and helpers"""
    idf_object = idf.newidfobject(c)
    name = py_class_name(c)
    # ---------- TypedDict ----------
    types_lines.append(f"class {name}Type(TypedDict, total=False):")
    types_lines.append(f'    """"dict for {name}"""')
    if not idf_object.fieldnames:
        types_lines.append("    pass")
    else:
        for f in idf_object.fieldnames:
            if BREAKOUT_PATTERN is not None and BREAKOUT_PATTERN in f:
                break
            py_name = clean_name(f)
            if py_name != "key":
                types_lines.append(f"    {py_name}: str | int | float")
    types_lines.append("")

    # ---------- Helper eppy ----------
    helpers_lines.append(f"def {name}(idf, **kwargs: Unpack[{name}Type]):")
    helpers_lines.append(f'    """"helper for {name}"""')
    helpers_lines.append(f"    return idf.newidfobject('{c}', **kwargs)")
    helpers_lines.append("")

def get_ep_version(idd_file: str) -> str | None:
    """get energyplus version from the idd file"""
    ep_version = None
    with open(idd_file, 'r', encoding="utf-8") as f:
        for line in f:
            if line.startswith("!IDD_Version"):
                ep_version = line.split(" ")[-1].strip().replace(".","_")
                print(f"Version d'EnergyPlus : {ep_version}")
                break
    return ep_version

def main(output: Path):
    """generate the helpers"""
    output.mkdir(exist_ok=True)

    # ---------- Load IDF ----------
    idf = IDF(IDF_PATH)
    all_classes = idf.idfobjects

    for c in sorted(all_classes):
        append(idf, c)

    # ---------- Write files ----------
    (output / f"{TYPES_NAME}.py").write_text("\n".join(types_lines), encoding="utf-8")
    (output / f"{HELPERS_NAME}.py").write_text("\n".join(helpers_lines), encoding="utf-8")

    print(f"✔ Helpers generated in {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="generate autocompletion python helpers for energyplus"
    )
    parser.add_argument(
        "--os_ep_path",
        action="store",
        help="energyplus absolute path",
        default=OS_EP_PATH
    )
    parser.add_argument(
        "--version",
        action="store",
        help="use folder structure using ep version number",
        default=True
    )
    args = parser.parse_args()

    IDD_FILE = f"{args.os_ep_path}/Energy+.idd"
    version = get_ep_version(idd_file=IDD_FILE)

    IDF.setiddname(IDD_FILE)

    if MANUAL:
        manual()
    else:
        OUTPUT_DIR = f"{REPO_ROOT}/src/idfhub/idf_autocomplete"
        if args.version and version is not None:
            OUTPUT_DIR = f"{OUTPUT_DIR}/v{version}"
        main(Path(OUTPUT_DIR))
