"""
Extraction des tests de réponse thermique (TRT)
depuis le WFS BRGM / ADEME.

Dépendances :
    pip install requests pandas
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import pandas as pd
import requests


WFS_URL = (
    "https://data.geoscience.fr/api/"
    "surfaceGeothermalResources/"
    "geothermalClosedLoopHeatExchanger/"
    "wfs"
)

OUTPUT = Path("trt_brgm.csv")

TIMEOUT = 60


def get_capabilities() -> str:
    """Récupère le document GetCapabilities du WFS."""

    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetCapabilities",
    }

    response = requests.get(
        WFS_URL,
        params=params,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.text


def find_trt_layer(xml_text: str) -> str:
    """
    Recherche la couche TEST_REPONSE_THERMIQUE dans GetCapabilities.

    Retourne son nom WFS exact.
    """

    root = ET.fromstring(xml_text)

    # Les namespaces peuvent varier selon le serveur.
    for element in root.iter():

        local_name = element.tag.split("}")[-1]

        if local_name != "Name":
            continue

        if element.text is None:
            continue

        name = element.text.strip()

        if "TEST_REPONSE_THERMIQUE" in name.upper():
            return name

    raise RuntimeError(
        "La couche TEST_REPONSE_THERMIQUE n'a pas été trouvée "
        "dans GetCapabilities."
    )


def get_features(
    layer_name: str,
    count: int = 10000,
) -> dict[str, Any]:
    """Télécharge les entités de la couche TRT en GeoJSON."""

    params = {
        "service": "WFS",
        "version": "2.0.0",
        "request": "GetFeature",
        "typeNames": layer_name,
        "outputFormat": "application/json",
        "count": count,
    }

    response = requests.get(
        WFS_URL,
        params=params,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def features_to_dataframe(
    data: dict[str, Any],
) -> pd.DataFrame:
    """Transforme le GeoJSON en DataFrame."""

    rows = []

    for feature in data.get("features", []):

        properties = feature.get("properties", {}).copy()

        geometry = feature.get("geometry")

        if geometry:
            coordinates = geometry.get("coordinates")

            if (
                geometry.get("type") == "Point"
                and coordinates
                and len(coordinates) >= 2
            ):
                properties["longitude"] = coordinates[0]
                properties["latitude"] = coordinates[1]

        rows.append(properties)

    return pd.DataFrame(rows)


def main() -> None:

    print("Connexion au WFS BRGM...")
    print(WFS_URL)
    print()

    # ------------------------------------------------------------------
    # 1. GetCapabilities
    # ------------------------------------------------------------------

    print("Récupération des capacités WFS...")

    capabilities = get_capabilities()

    layer_name = find_trt_layer(capabilities)

    print(f"Couche TRT trouvée : {layer_name}")
    print()

    # ------------------------------------------------------------------
    # 2. GetFeature
    # ------------------------------------------------------------------

    print("Téléchargement des TRT...")

    data = get_features(layer_name)

    features = data.get("features", [])

    print(f"Nombre de TRT récupérés : {len(features)}")

    # ------------------------------------------------------------------
    # 3. DataFrame
    # ------------------------------------------------------------------

    df = features_to_dataframe(data)

    print(f"Nombre de colonnes : {len(df.columns)}")
    print()
    print("Champs disponibles :")

    for column in df.columns:
        print(f"  - {column}")

    # ------------------------------------------------------------------
    # 4. Export
    # ------------------------------------------------------------------

    df.to_csv(
        OUTPUT,
        index=False,
        encoding="utf-8-sig",
    )

    print()
    print(f"Fichier écrit : {OUTPUT.resolve()}")


if __name__ == "__main__":
    main()
