from eppy.modeleditor import IDF

from idfhub.helpers.consts import REPO_ROOT

BUILDING_NAME = "batiment_600m2"
OS_EP_PATH = "C:/openstudioapplication-1.8.0/EnergyPlus"
IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
idf = IDF(f"{REPO_ROOT}/{BUILDING_NAME}.idf")
