"""trt map"""
from pathlib import Path

import folium
import pandas as pd
import xyzservices.providers as xyz


TRT_CSV = Path("trt_brgm.csv")
OUTPUT_HTML = Path("trt_map.html")


def main() -> None:
    df = pd.read_csv(TRT_CSV)

    # Coordonnées
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")

    df = df.dropna(subset=["longitude", "latitude"])

    # Centre de la France
    m = folium.Map(
        location=[46.6, 2.3],
        zoom_start=6,
        tiles="https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png",
        attr="© OpenStreetMap contributors",
        #tiles=xyz.Esri.WorldGrayCanvas.build_url(),
        #attr=xyz.Esri.WorldGrayCanvas.html_attribution,
        control_scale=True,
    )

    # TRT
    for _, row in df.iterrows():

        def value(column: str) -> str:
            value = row.get(column, "")
            if pd.isna(value):
                return ""
            return str(value)

        popup_html = f"""
        <div style="font-size: 13px;">
            <h4 style="margin-bottom: 8px;">
                TRT {value("id_test")}
            </h4>

            <b>Borehole :</b> {value("id_borehole")}<br>
            <b>Profondeur :</b> {value("profondeur_sonde")} m<br>
            <b>Durée :</b> {value("duree_test")} h<br>
            <b>Température terrain :</b> {value("temp_terrain")} °C<br>
            <b>Conductivité :</b> {value("cond_therm")} W/(m·K)<br>
            <b>Résistance sonde :</b> {value("rb_sonde")} m·K/W<br>
            <b>Capacité volumique :</b>
                {value("cp_chaleur_specif")} MJ/(m³·K)<br>
            <b>Lithologie :</b> {value("litho_dominante")}<br>
            <br>
            <b>Coordonnées :</b><br>
            {value("latitude")}, {value("longitude")}
        </div>
        """

        popup = folium.Popup(
            popup_html,
            max_width=400,
        )

        folium.CircleMarker(
            location=[
                row["latitude"],
                row["longitude"],
            ],
            radius=5,
            popup=popup,
            tooltip=f"TRT {value('id_test')}",
            fill=True,
        ).add_to(m)

    m.save(OUTPUT_HTML)

    print(f"{len(df)} TRT affichés")
    print(f"Carte : {OUTPUT_HTML.resolve()}")


if __name__ == "__main__":
    main()
