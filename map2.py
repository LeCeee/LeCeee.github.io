import folium
import pandas
import phonenumbers

data = pandas.read_csv("predictionsWeb.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
city = list(data["city"])
helpn = list(data["helplineNumber"])
stat = list(data["UNSAFE"])
hosp = list(data["hospital"])
hospc = list(data["hospitalContact"])
pols = list(data["policeStation"])

# print(type(helpn))
for idx in range(len(helpn)):
    helpn[idx] = '011'+ str(helpn[idx])
    hospc[idx] = '011'+ str(hospc[idx])


# print(helpn)
    # print(n)

# elev = list(data["ELEV"])
# name = list (data["NAME"])
def color_prod (st) :
    if st == 1.0 :
        return "green"
    else : return "red"


map = folium.Map(location =[28.67, 77.09], zoom_start = 15, tiles = "Mapbox Street", API_key = 'pk.eyJ1IjoiY2VlZSIsImEiOiJjam1sc2lmaWwwYXAxM3FvYWN2dTh3ejNjIn0.efl2Y5sXJ_58TCpNhpSVbg', attr='Mapbox Data Attribution')
fg = folium.FeatureGroup(name = "My Map2")

for lt ,ln ,st,hn,hos, hosc, pol, ct in zip(lat,lon,stat,helpn,hosp,hospc,pols,city) :
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(f' Area : {ct}, Nearest police station: {pol} Helpline Number :{str(hn)}, Nearest hospital : {str(hos)} Helpline number : {hosc}',parse_html=True), icon=folium.Icon(color=color_prod(st))))


map.add_child(fg)
folium.TileLayer('openstreetmap').add_to(map)
map.save("index.html")