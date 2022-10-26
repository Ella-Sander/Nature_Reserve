import webbrowser
import os
import pandas as pd
import folium
import consts
from folium.features import DivIcon

def run_map():
    Nature_reserves_file = consts.NATURE_RESERVES_FILE
    Nature_reserves = pd.read_csv(Nature_reserves_file)

    map = folium.Map(location=[Nature_reserves.Zip_Code_X.mean(), Nature_reserves.Zip_Code_Y.mean()],
                     zoom_start=8, control_scale=True)

    for index, location_info in Nature_reserves.iterrows():
        link_and_name = '<a href=\"' + location_info["Link"] + '\">' + location_info["Name"] + '</a>'

        if location_info["Status"]:
            folium.Marker([location_info["Zip_Code_X"], location_info["Zip_Code_Y"]],
                          icon=folium.Icon(icon="leaf", icon_color="black", color="green", prefix="fa"),
                          popup=link_and_name, tooltip=location_info["Name"]).add_to(map)
        else:
            folium.Marker([location_info["Zip_Code_X"], location_info["Zip_Code_Y"]],
                          icon=folium.Icon(icon="warning", icon_color="black", color="red", prefix="fa"),
                          popup=link_and_name, tooltip=location_info["Name"]).add_to(map)

    map.save("index.html")

    filename = 'file:///' + os.getcwd() + '/' + 'index.html'
    webbrowser.open_new_tab(filename)
