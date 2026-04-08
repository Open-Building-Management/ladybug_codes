"""yml management"""
import os
import sys
import yaml

from eppy.modeleditor import IDF

from idfhub.helpers.consts import REPO_ROOT

def load_config(repo_root: str) -> dict:
    """Load configuration.yml."""
    yaml_path = f"{repo_root}/configuration.yml"
    if os.path.exists(yaml_path):
        with open(yaml_path, "r", encoding="utf-8") as f:
            return dict(yaml.safe_load(f))
    return {}

CONF = load_config(REPO_ROOT)
REQUIRED = [
    "building_name",
    "name",
    "suffix",
    "os_ep_path",
    "zones",
    "loops",
    "branches",
    "equipments"
]
for element in REQUIRED:
    if element not in CONF:
        sys.exit()

BUILDING_NAME: str = CONF["building_name"]
ZONES = CONF["zones"]
LOOPS: list[str] = CONF["loops"]
BRANCHES: dict[str, dict[str, list[str]]] = CONF["branches"]
EQUIPMENTS: list[str] = CONF["equipments"]

PROJECT_NAME = f"{CONF['name']}_{CONF['suffix']}"
OS_EP_PATH = CONF["os_ep_path"]
IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
idf = IDF(f"{REPO_ROOT}/{BUILDING_NAME}.idf")

