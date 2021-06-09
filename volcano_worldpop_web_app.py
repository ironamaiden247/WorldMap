import folium
import pandas as pd

df=pd.read_csv('Volcanoes.txt')
##-------Old Version---------------------------
# calculating the mean of the latitudes
# and longitudes of the locations of volcanoes
latmean=df['LAT'].mean()
lonmean=df['LON'].mean()

map2 = folium.Map(location=[latmean,lonmean],
        zoom_start=6,tiles = 'Stamen Terrain', attr='None')



# Function to change the marker color
# according to the elevation of volcano
def color(elev):
    if elev in range(0,1000):
        col = 'green'
    elif elev in range(1001,1999):
        col = 'blue'
    elif elev in range(2000,2999):
        col = 'orange'
    else:
        col='red'
    return col

fgv=folium.FeatureGroup(name='US Volcanoes')


# Iterating over the LAT,LON,NAME and
# ELEV columns simultaneously using zip()
for lat, lan, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    # Marker() takes location coordinates
    # as a list as an argument
    fgv.add_child(folium.Marker(location=[lat, lan], popup=name,
                  icon=folium.Icon(color=color(elev),
                                   icon_color='yellow', icon='cloud')))


fgp=folium.FeatureGroup(name='World Population')


fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
               style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
               else 'yellow' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map2.add_child(fgv)
map2.add_child(fgp)
map2.add_child(folium.LayerControl())
# Save the file created above
map2.save('test2.html')
