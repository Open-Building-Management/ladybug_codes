"""yml management"""
import argparse
import ast
import logging
import operator as op
import os
import re
import sys
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
            return yaml.safe_load(f) or {}
    return {}

OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

hvac_parser = argparse.ArgumentParser(description='hvac configuration')

hvac_parser.add_argument(
    "--conf",
    action="store",
    help="yml configuration file",
    default="configuration.yml"
)

hvac_parser.add_argument(
    "--geoconf",
    action="store",
    help="geometry configuration file",
    default="conf_geometry/agence.yml"
)

# Parse arguments, but catch errors (for pytest which passes its own args)
try:
    args = hvac_parser.parse_args()
except SystemExit:
    # Use defaults when argument parsing fails (e.g., in pytest)
    args = argparse.Namespace(conf="configuration.yml", geoconf="conf_geometry/agence.yml")

CONF = load_config(REPO_ROOT, args.conf)
GEOMETRY = load_config(REPO_ROOT, args.geoconf)
COMMON_HEIGHT = GEOMETRY.get("height", 3)
BLOCKS = GEOMETRY.get("blocks", {})

def _get_dependencies(expr: str) -> set[str]:
    """extraction des noms utilisés dans une expression"""
    tree = ast.parse(expr, mode="eval")
    return {
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name)
    }

def _resolve(key: str, metadata: dict, resolved: dict, resolving: set):
    """résolution d'une clé"""
    if key in resolved:
        return resolved[key]

    if key in resolving:
        raise ValueError(f"circular dependency involving {key}")

    value = metadata[key]

    if not isinstance(value, str):
        resolved[key] = value
        return value

    resolving.add(key)

    dependencies = _get_dependencies(value)

    variables = {
        dep: _resolve(dep, metadata, resolved, resolving)
        for dep in dependencies
    }

    result = eval_expr(value, variables)

    resolving.remove(key)
    resolved[key] = result

    return result

def _is_variable(key: str):
    """détection des variables autorisées"""
    if key in {"height", "altitude"}:
        return True
    return any(
        re.match(fr"^{prefix}[0-9]+$", key)
        for prefix in ("d", "z", "h")
    )

def get_variables(metadata: dict) -> dict:
    """return dict of variables"""
    resolved: dict = {}
    for key in metadata:
        if _is_variable(key):
            _resolve(key, metadata, resolved, set())
    return resolved

def get_variables_old(metadata: dict) -> dict:
    """return dict of variables"""
    variables = {}
    formulas = {}
    accepted_keys = [
        "height",
        "altitude",
    ]
    for key in metadata:
        if key in accepted_keys:
            if isinstance(metadata[key], str):
                formulas[key] = metadata[key]
            else:
                variables[key] = metadata[key]
        for start in ["d", "z", "h"]:
            pattern = f"^{start}[0-9]+"
            if re.match(pattern, key):
                if isinstance(metadata[key], str):
                    formulas[key] = metadata[key]
                else:
                    variables[key] = metadata[key]
    resolved = {
        key:eval_expr(formula, variables)
        for key,formula in formulas.items()
    }
    return {**variables, **resolved}

def eval_expr(expr, variables):
    """secure resolution engine"""
    def _eval(node):
        """evaluation method"""
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.Name):
            return variables[node.id]

        if isinstance(node, ast.BinOp):
            return OPS[type(node.op)](
                _eval(node.left),
                _eval(node.right)
            )

        if isinstance(node, ast.UnaryOp):
            return OPS[type(node.op)](_eval(node.operand))

        raise TypeError(f"Unsupported Expression : {ast.dump(node)}")

    return _eval(ast.parse(expr.strip(), mode="eval").body)

REQUIRED = [
    "building_name",
    "name",
    "suffix",
    "os_ep_path",
    "zones",
    "loops",
    "equipments",
]

for required_key in REQUIRED:
    if required_key not in CONF:
        print(f"exiting - check conf {required_key} is missing")
        sys.exit()

BUILDING_NAME: str = CONF["building_name"]
ZONES = CONF["zones"]
LOOPS: list[str] = CONF["loops"]
EQUIPMENTS: list[str] = CONF["equipments"]
AIRLOOPS: list[str] = CONF.get("airloops", [])

PROJECT_NAME = f"{CONF['name']}_{CONF['suffix']}"
OS_EP_PATH = CONF["os_ep_path"]
IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
try:
    idf = IDF(f"{REPO_ROOT}/{BUILDING_NAME}.idf")
except FileNotFoundError:
    idf = None

# par défaut, 20°C chauffage et 25°C raffraichissement
SCHEDULES: dict[str, dict] = {
    "heating": {
        "mode": "compact",
        "confort": 20,
        "standby": 0
    },
    "cooling": {
        "mode": "constant",
        "confort": 25,
        "standby": 25
    }
}

YML_SCHED = CONF.get("schedules", {})
for sched_name, sched_conf in YML_SCHED.items():
    if sched_name not in ["heating", "cooling"]:
        continue
    for yml_key, yml_value in sched_conf.items():
        SCHEDULES[sched_name][yml_key] = yml_value

RUN_PERIOD = CONF.get("run_period", {})

required = [
    "Begin_Month",
    "Begin_Day_of_Month",
    "Begin_Year",
    "End_Month",
    "End_Day_of_Month",
    "End_Year"
]

DEF_RUN_PERIOD = {
    "Begin_Month": 1,
    "Begin_Day_of_Month": 1,
    "Begin_Year": 2026,
    "End_Month": 12,
    "End_Day_of_Month": 31,
    "End_Year": 2026
}

for el in required:
    if el not in RUN_PERIOD:
        RUN_PERIOD[el] = DEF_RUN_PERIOD[el]
