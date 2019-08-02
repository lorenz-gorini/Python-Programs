import lib.osm as osm

#----------------------------------------------------------------
#Insert city names separated by commas and it calculates the distance between they 
#(in direct line) using the OpenStreetMap API.
#AUTHOR: Adolfo Andres Garcia Galache  -- hola@adolfoandres.es
#----------------------------------------------------------------
#----------------------------------------------------------------


#There's is a library to calculate the distance between two cities using the
# Haversine formula. This library is made by Bartek Gorny and is free software.

#There's also another little library written by me (called osm) to recieve the 
#json from the server and calculate the distance.

#If you redristribute the software. Please do it under GPLv3 or use another
# library to calculate the direct line distance.


str_c = input("insert two or more city names separated by commas:\n")

cities = str_c.split(',')

threeCorrCities, twoCorrCities , dist = osm.distance(cities)

if (not (twoCorrCities or threeCorrCities)):
    print ("The distance connecting the cities is: {} km".format(dist))
elif twoCorrCities:
    print (twoCorrCities)
    print ("The distance connecting the different cities is: {} km".format(dist))
elif threeCorrCities:
    print (threeCorrCities)
