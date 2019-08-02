# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:50:19 2019

@author: loreg
"""
import time

import requests
import json
import lib.points2distance as points2distance
"""
Declare variables of a "good" city name, where the lat and long exist,
in order to eliminate the problem of a "bad" city name
"""
goodLat=0
goodLon=0

def get_iss_json():
    r=requests.get('http://api.open-notify.org/iss-now.json')
    return r.json()
"""
Get the coordinates from json in degree units (floating point format)
"""
def get_lon_lat(iss_json):
    lon=float(iss_json['iss_position']['longitude'])
    lat=float(iss_json['iss_position']['latitude'])
    return lon,lat

def convert_km_h(speed):
    #from km/s to km/h
    speed=speed*3600
    return speed

"""
THIS IS THE FUNCTION CALLED FROM MAIN AND IT CALCULATES THE DISTANCE BETWEEN THE 
TWO COORDINATES (start,end). IT GETS THE VALUES FROM THE TWO METHODS ABOVE.

SINCE THE ALTITUDE IS NOT CONTAINED IN JSON DATA, IT USES THE ACTUAL ALTITUDE
VALUE (even though it is slowly changing over time due to friction) = 405.8
 
FOR THE SAME REASON I WILL APPROXIMATE THE ISS MOTION TO A CIRCULARLY-SHAPED 
ORBIT.
"""

"""        
I WANT TO HANDLE THE CASE WHERE THE COORDINATES ARE WRONG. 
I SIMPLY GO ON IN THE CYCLE (it doesn't save any data 
and it doesn't change any value like totPath or time, otherwise it may change the 
final avg speed value)
"""
def avg_speed(tot_time):
    iss_before=0
    iss_now=0
    tot_distance=0
    bad_value=True
    points=[]
    #two moments to calculate the intervals
    """
    end_time is not initial_time+tot_time because I may not get the final
    value (or even no values at all)
    """
    final_time=0
    initial_time=0
    #get the first good value and start the timer (get initial value)
    while (bad_value):
      #  try:
            iss_before=get_lon_lat(get_iss_json())
            points.append(iss_before)
            print(iss_before)
            bad_value=False
            initial_time=time.time()
      #  except:
          #  continue
    #count of the considered values
    num_values=0
    """
    I decided to stop the cycle after the chosen time
    I could also decide to choose only the time when I get good values (but it could get stuck, 
    instead I only tell the users how many values I got, and if the program didn't get
    any values)
    """
    while ((final_time-initial_time)<(tot_time+1)):
       # try:
            time.sleep(1)
            iss_now=get_lon_lat(get_iss_json())
            points.append(iss_now)
            print(iss_now)
            if (iss_before!=iss_now):
                tot_distance=tot_distance+points2distance.distance(iss_before,iss_now)
                final_time=time.time()
                num_values=num_values+1
            iss_before=iss_now
      #  except:
           # continue;
    avg_speed=tot_distance/(final_time-initial_time)
    return num_values,convert_km_h(avg_speed),points

