"""common methods"""
import os
import logging

from honeybee.model import Model

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

def view_boundaries(building: Model):
    """check boundary conditions"""
    for element in building:
        for face in element.faces:
            message = f"id: {face.identifier} type: {type(face.type)}"
            LOGGER.info(message)
            message = f"bc: {face.boundary_condition}"
            LOGGER.info(message)
            message = f"material: {face.properties.energy.construction.identifier}"
            LOGGER.info(message)

class ColorFormatter(logging.Formatter):
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
    name: str|None = None,
    format: str = FORMAT,
    level: int = logging.DEBUG,
) -> logging.Logger:
    """get a logger"""
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter(format))
    handler.setLevel(level)
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger