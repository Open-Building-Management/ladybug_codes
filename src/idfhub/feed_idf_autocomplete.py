"""generate helpers to autocomplete EP classes and objects"""
from __future__ import annotations
from pathlib import Path
import re
from eppy.modeleditor import IDF

from idfhub.helpers.consts import REPO_ROOT

# ---------------- CONFIG ----------------
OS_EP_PATH = "C:/openstudioapplication-1.8.0/EnergyPlus"
IDD_PATH = f"{OS_EP_PATH}/Energy+.idd"
IDF_PATH = f"{REPO_ROOT}/batiment_600m2.idf"
OUTPUT_DIR = Path(f"{REPO_ROOT}/src/idfhub/idf_autocomplete")
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
                types_lines.append(f"    {py_name}: str")
    types_lines.append("")

    # ---------- Helper eppy ----------
    helpers_lines.append(f"def {name}(idf, **kwargs: {name}Type):")
    helpers_lines.append(f'    """"helper for {name}"""')
    helpers_lines.append(f"    return idf.newidfobject('{c}', **kwargs)")
    helpers_lines.append("")

def main():
    """generate the helpers"""
    OUTPUT_DIR.mkdir(exist_ok=True)

    # ---------- Load IDF ----------
    idf = IDF(IDF_PATH)
    all_classes = idf.idfobjects

    for c in sorted(all_classes):
        append(idf, c)

    # ---------- Write files ----------
    (OUTPUT_DIR / f"{TYPES_NAME}.py").write_text("\n".join(types_lines), encoding="utf-8")
    (OUTPUT_DIR / f"{HELPERS_NAME}.py").write_text("\n".join(helpers_lines), encoding="utf-8")

    print(f"✔ Helpers generated in {OUTPUT_DIR}")

if __name__ == "__main__":
    IDF.setiddname(IDD_PATH)
    if MANUAL:
        manual()
    else:
        main()
