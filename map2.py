import folium
import pandas

data = pandas.read_csv("predictionSmall.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
stat = list(data["UNSAFE"])
# elev = list(data["ELEV"])
# name = list (data["NAME"])
def color_prod (st) :
    if st == 1.0 :
        return "green"
    else : return "red"


map = folium.Map(location =[28.68, 77.01], zoom_start = 11, tiles = "Mapbox Street", API_key = 'pk.eyJ1IjoiY2VlZSIsImEiOiJjam1sc2lmaWwwYXAxM3FvYWN2dTh3ejNjIn0.efl2Y5sXJ_58TCpNhpSVbg', attr='Mapbox Data Attribution')
fg = folium.FeatureGroup(name = "My Map2")
for lt ,ln ,st in zip(lat,lon,stat) :
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(f'status : {st}',parse_html=True), icon=folium.Icon(color=color_prod(st))))

    # if st == 1.0 :
    #     fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(f'status : {st}',parse_html=True), icon=folium.Icon(color='green')))
    # else :
    #     fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(f'status : {st}',parse_html=True), icon=folium.Icon(color='red')))

map.add_child(fg)
folium.TileLayer('openstreetmap').add_to(map)
map.save("Map2.html")