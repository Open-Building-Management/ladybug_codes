"""consts"""
import logging
from idfhub.helpers.common import parent_dir

FORMAT = '%(asctime)s %(levelname)-8s %(threadName)-10s %(module)-10s %(funcName)s %(message)s'
logging.basicConfig(format=FORMAT)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel("INFO")

REPO_ROOT = parent_dir(__file__, 4)

