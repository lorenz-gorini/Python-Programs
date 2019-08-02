# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:16:27 2019

@author: loreg
"""


from gmplot import gmplot

points=[(45.500428, 9.268353), (46.500428, 10.268353), (-118.846, -44.2978), (-118.7345, -44.2493), (-118.6233, -44.2007), (-118.5122, -44.152)]
#╔def drawISS(points):
# Place map
gmap = gmplot.GoogleMapPlotter(points[0][0], points[0][1],2)

# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*points)
gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=80)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*points)
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=90, marker=False)

# Marker
hidden_gem_lat, hidden_gem_lon = points[0][0], points[0][1]
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")
