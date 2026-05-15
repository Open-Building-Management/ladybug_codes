"""yml management"""
import argparse
import logging
import os
import sys
from typing import Any
import yaml

from eppy.modeleditor import IDF

FORMAT = (
    '%(asctime)s | %(levelname).1s | '
    '%(name)s:%(lineno)d | '
    '%(funcName)s() | '
    '%(message)s'
)

LOGGER = logging.getLogger(__name__)

def parent_dir(path, levels=1) -> str:
    """Retourne le path du répertoire parent 
    jusqu'au niveau fourni en argument
    """
    for _ in range(levels):
        path = os.path.dirname(path)
    return path

REPO_ROOT = parent_dir(__file__, 3)

class ColorFormatter(logging.Formatter):
    """logging color formatter"""
    COLORS = {
        logging.DEBUG: "\033[90m",   # gris
        logging.INFO: "\033[36m",    # cyan
        logging.WARNING: "\033[33m", # jaune
        logging.ERROR: "\033[31m",   # rouge
        logging.CRITICAL: "\033[41m",
    }
    RESET = "\033[0m"

    def format(self, record):
        color = self.COLORS.get(record.levelno, "")
        msg = super().format(record)
        return f"{color}{msg}{self.RESET}"

def get_logger(
    log_name: str|None = None,
    log_format: str = FORMAT,
    log_level: int = logging.DEBUG,
) -> logging.Logger:
    """get a logger"""
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter(log_format))
    handler.setLevel(log_level)
    logger = logging.getLogger(log_name)
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(log_level)
    logger.propagate = False
    return logger


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
try:
    idf = IDF(f"{REPO_ROOT}/{BUILDING_NAME}.idf")
except FileNotFoundError:
    idf = None

if SENSORS:
    for conf in SENSORS.values():
        if "type" not in conf:
            print("exiting - specify sensor type")
            sys.exit()
        if conf["type"] != "Site Outdoor Air Drybulb Temperature":
            if "loop" not in conf:
                print("exiting - specify loop")
                sys.exit()
