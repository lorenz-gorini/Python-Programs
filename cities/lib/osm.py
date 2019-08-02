import requests
import json
import lib.coord as coord

"""
Declare variables of a "good" city name, where the lat and long exist,
in order to eliminate the problem of a "bad" city name
"""
goodLat=0
goodLon=0

def get_city_json(city_name):
    r=requests.get('https://nominatim.openstreetmap.org/search?q='+city_name+'&format=json')
    return r.json()

def get_lon_lat(city_json):

        """
        assuming the correct SOLUTION IS ALWAYS THE FIRST ONE, PROPOSED FROM THE SITE
        """
        lat=city_json[0]['lat'] 
        lon=city_json[0]['lon']
        return float(lon),float(lat)

"""        
I WANT TO HANDLE THE CASE WHERE THE NAMES OF THE CITIES WERE WRONG AND THE 
SITE DIDN'T RETURN ANY USEFUL DATA.
I RETURN ONLY THE GOOD CITY NAME (where lat and lon exist)
"""
def good_city_names(cities):
    city_lon_lat=[]
    num_cities=0
    for i in range(len(cities)):
        try:
            city_lon_lat.append(get_lon_lat(get_city_json(cities[i])))
            num_cities=num_cities+1
        except:
            print ("the name of one (or more) city was not found in the database")
    # case where the available cities are not enough
    if (num_cities<=1):
        city_lon_lat=0
    return city_lon_lat
    
"""
THIS IS THE FUNCTION CALLED FROM MAIN AND IT ASSIGNS THE COORDINATES OF THE 
INPUT CITIES TO THE VARIABLES (start,end). 
IT CALLS THE THREE METHODS ABOVE TO GET THE DATA
"""
def distance(cities):
    city_lon_lat=good_city_names(cities)
    dist=0
    totdist=0
    twoCorrCities=False
    threeCorrCities=False
    num=0
    if (city_lon_lat==0):
        threeCorrCities="Only one or none of the input city names is valid. ",
        "No result can be calculated"
    else:
        for i in range(len(city_lon_lat)-1): 
                start=city_lon_lat[i]
                end=city_lon_lat[i+1]
                dist=coord.points2distance(((start[0],0,0),(start[1],0,0)),((end[0],0,0),(end[1],0,0)))
                if dist==0:
                    twoCorrCities=True;
                totdist=totdist+dist
        if (totdist<0.00001):
            twoCorrCities=False
            threeCorrCities="The three cities correspond, so their distance is 0 km"
        elif twoCorrCities:
            twoCorrCities="Two cities inserted correspond to the same city (it is good to be informed)"
    
    return threeCorrCities,twoCorrCities,totdist
    
