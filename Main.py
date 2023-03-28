import folium
import pandas

# data loading with pandas library
data = pandas.read_csv("places.txt")
lat = data["LAT"]
lon = data["LON"]
type = data["TYPE"]
name = data["NAME"]
desc = data["DESC"]
link = data["LINK"]

# creating a map with folium library
map = folium.Map(location=[52.5107, 13.3830], zoom_start = 11, min_zoom = 10, 
                min_lat = 52.2, max_lat = 52.8, 
                min_lon = 13, max_lon = 13.7,
                max_bounds = True, min_bounds = True )

# function which creates various feature groups
def groups(type):
    return folium.FeatureGroup(type)

#festure groups
fg_food = groups("Food")
fg_sightseeing = groups("Sightseeing")
fg_relax = groups("Relax")
fg_party = groups("Party")
fg_museum = groups("Museums")

# Popup style with html
html = """<body style="background-color:#FFF8DC">
<h4 style="color:%s; font-size:24; font-style:italic; font-family:verdana"> %s </h4>
<p>%s</p> 
<p><a href="%s" target="_blank" > More </a></p>
</body>
"""

# function which creates Markers for different feature groups with parameters for the groups, markers colors and icons
def marker_type(feature_group, marker_color, marker_icon):
    iframe = folium.IFrame(html=html % (marker_color, name, desc, link), width=400, height=200)
    feature_group.add_child(folium.Marker(location = [lat,lon], popup=folium.Popup(iframe), icon=folium.Icon(color = marker_color,icon=marker_icon)))
        
        
# loop which creates Markers and puts name,desc,link into html iframe, lat and lon into marker position and divide feature groups based on type
for name,desc,link,type,lat,lon in zip(name,desc,link,type,lat,lon):
    if type == "Food":
        marker_type(fg_food, "orange", "glyphicon-cutlery")
    elif type == "Relax":
        marker_type(fg_relax, "blue", "glyphicon-leaf")
    elif type == "Sightseeing":
        marker_type(fg_sightseeing, "green", "glyphicon-eye-open")
    elif type == "Party":
        marker_type(fg_party, "red", "glyphicon-fire")
    elif type == "Museums":
        marker_type(fg_museum, "purple", "glyphicon-picture" )

# adding features into the map
map.add_child(fg_food)
map.add_child(fg_sightseeing)
map.add_child(fg_relax)
map.add_child(fg_party)
map.add_child(fg_museum)
map.add_child(folium.LayerControl())

# saving the map
map.save("BerlinFun.html")
