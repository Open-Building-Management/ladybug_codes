"""generate helpers to autocomplete EP classes and objects"""
from __future__ import annotations
from pathlib import Path
from eppy.modeleditor import IDF
import re

from helpers.consts import REPO_ROOT

# ---------------- CONFIG ----------------
OS_EP_PATH = "C:/openstudioapplication-1.8.0/EnergyPlus"
IDD_PATH = f"{OS_EP_PATH}/Energy+.idd"
IDF_PATH = f"{REPO_ROOT}/batiment_600m2_windows_b.idf"
OUTPUT_DIR = Path(f"{REPO_ROOT}/src/idf_autocomplete")
MANUAL = False
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

def main():
    """generate the helpers"""
    OUTPUT_DIR.mkdir(exist_ok=True)

    # ---------- Load IDF ----------
    idf = IDF(IDF_PATH)

    types_lines = [
        "from __future__ import annotations",
        "from typing import TypedDict, Literal",
        "",
    ]

    helpers_lines = [
        "from __future__ import annotations",
        "from .idf_types import *",
        "",
    ]

    all_classes = idf.idfobjects

    for c in sorted(all_classes):
        # create dummy object to get fields
        dummy = idf.newidfobject(c)
        class_name = py_class_name(c)

        # ---------- TypedDict ----------
        types_lines.append(f"class {class_name}Type(TypedDict, total=False):")
        if not dummy.fieldnames:
            types_lines.append("    pass")
        else:
            for f in dummy.fieldnames:
                py_name = clean_name(f)
                if py_name != "key":
                    types_lines.append(f"    {py_name}: str")  # type simplifié, on pourrait raffiner
        types_lines.append("")

        # ---------- Helper eppy ----------
        helpers_lines.append(f"def {class_name}(idf, **kwargs: {class_name}Type):")
        helpers_lines.append(f"    return idf.newidfobject('{c}', **kwargs)")
        helpers_lines.append("")

    # ---------- Write files ----------
    (OUTPUT_DIR / "idf_types.py").write_text("\n".join(types_lines), encoding="utf-8")
    (OUTPUT_DIR / "idf_helpers.py").write_text("\n".join(helpers_lines), encoding="utf-8")

    print(f"✔ Helpers generated in {OUTPUT_DIR}")

if __name__ == "__main__":
    IDF.setiddname(IDD_PATH)
    if MANUAL:
        manual()
    else:
        main()
