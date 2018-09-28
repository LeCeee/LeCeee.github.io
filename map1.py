import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list (data["NAME"])

map = folium.Map(location =[38.58, -99.01], zoom_start = 6, tiles = "Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
for lt ,ln ,el, nm in zip(lat,lon,elev,name) :
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup("name:{nm}</br>"  "elevation :{str(el)}",parse_html=True), icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map1.html")