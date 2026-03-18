"""yml management"""
import os
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

BUILDING_NAME = CONF.get("building_name")
hvac_setup = CONF.get("hvac_setup")
HVAC_USER_CONF = CONF.get(hvac_setup)

PROJECT_NAME = f"{hvac_setup}_{HVAC_USER_CONF['suffix']}"
OS_EP_PATH = CONF.get("os_ep_path")
IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
idf = IDF(f"{REPO_ROOT}/{BUILDING_NAME}.idf")
