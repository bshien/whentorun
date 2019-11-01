import geocoder

g = geocoder.arcgis('Pleasanton, CA')
print(g.latlng)