"""yml management"""
import argparse
import os
import sys
from typing import Any
import yaml

from eppy.modeleditor import IDF

from idfhub.helpers.consts import REPO_ROOT

def load_config(repo_root:str, file_name:str = "configuration.yml") -> dict:
    """Load configuration.yml."""
    yaml_path = f"{repo_root}/{file_name}"
    if os.path.exists(yaml_path):
        with open(yaml_path, "r", encoding="utf-8") as f:
            return dict(yaml.safe_load(f))
    return {}

hvac_parser = argparse.ArgumentParser(description='hvac configuration')

hvac_parser.add_argument(
    "--conf",
    action="store",
    help="yml configuration file",
    default="configuration.yml"
)

args = hvac_parser.parse_args()

CONF = load_config(REPO_ROOT, args.conf)
REQUIRED = [
    "building_name",
    "name",
    "suffix",
    "os_ep_path",
    "zones",
    "loops",
    "equipments",
    "sensors"
]
for key in REQUIRED:
    if key not in CONF:
        print("exiting - check conf")
        sys.exit()

BUILDING_NAME: str = CONF["building_name"]
ZONES = CONF["zones"]
LOOPS: list[str] = CONF["loops"]
EQUIPMENTS: list[str] = CONF["equipments"]
SENSORS: dict[str, dict[str, Any]] = CONF["sensors"]

PROJECT_NAME = f"{CONF['name']}_{CONF['suffix']}"
OS_EP_PATH = CONF["os_ep_path"]
IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
idf = IDF(f"{REPO_ROOT}/{BUILDING_NAME}.idf")

if SENSORS:
    for conf in SENSORS.values():
        for key in ["loop", "port", "side", "type"]:
            if key not in conf:
                print("exiting - check conf")
                sys.exit()
