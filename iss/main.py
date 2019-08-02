# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:50:19 2019

@author: loreg
"""

import lib.path as path

#There's is a library to calculate the distance between two points of the ISS using the
# Haversine formula. This library is made by Bartek Gorny and is free software.

#There's also some little libraries written by me (called osm) to receive the 
#json from the server and calculate the distance.

#If you redistribute the software. Please do it under GPLv3 or use another
# library to calculate the direct line distance.


tot_time = int(input("insert the total time after which the program measures the average speed (in seconds)\n"))

num_values,avg_speed,points=path.avg_speed(tot_time)
if (num_values!=0):
    print("During the last {} seconds, the program detected {} positions of the ISS.".format(tot_time,num_values+1),
          "The average speed of the ISS  is: {} km/h".format(avg_speed))
    print(points)
   # draw.drawISS(points)



