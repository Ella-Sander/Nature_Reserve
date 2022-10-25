import webbrowser
import os
import pandas as pd
import folium

location = r"C:\Users\jbt\Downloads\Nature reserve (2).csv"
locations = pd.read_csv(location)

locations = locations[["Zip_Code_X", "Zip_Code_Y", "Name", "Link"]]

map = folium.Map(location=[locations.Zip_Code_X.mean(), locations.Zip_Code_Y.mean()],
                 zoom_start=8, control_scale=True)

red_icon = folium.Icon(color='red', icon= 'clean_icon.png')
green_icon = folium.Icon(color='green', icon= 'dirty_icon.png')

icon1 = folium.features.CustomIcon('clean_icon.png', icon_size=(60,60))

for index, location_info in locations.iterrows():
    folium.Marker([location_info["Zip_Code_X"], location_info["Zip_Code_Y"]], icon=folium.Icon(color='red',  icon='clean_icon.png'), popup= (location_info["Name"] + location_info["Link"])).add_to(map)

# m = folium.Map(location = [31.0208, 34.861])
map.save("index.html")

filename = 'file:///' + os.getcwd() + '/' + 'index.html'
webbrowser.open_new_tab(filename)
