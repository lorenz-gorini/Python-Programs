
"""
Created on Wed Jan 16 14:24:41 2019

@author: loreg
"""

#coding:UTF-8
"""
  Python implementation of Haversine formula
  Copyright (C) <2009>  Bartek Górny <bartek@gorny.edu.pl>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import math
      
def distance(start,end):
  """
    Calculate distance (in kilometers) between two points given as (long, latt) pairs
    based on Haversine formula (http://en.wikipedia.org/wiki/Haversine_formula).
    Implementation inspired by JavaScript implementation from http://www.movable-type.co.uk/scripts/latlong.html
    IT RETURNS THE DISTANCE IN KILOMETERS
    Accepts coordinates as tuples (deg, min, sec), but coordinates can be given in any form - e.g.
    can specify only minutes:
    (0, 3133.9333, 0) 
    is interpreted as 
    (52.0, 13.0, 55.998000000008687)
    which, not accidentally, is the lattitude of Warsaw, Poland.
  """
  start_long = math.radians(start[0])
  start_latt = math.radians(start[1])
  end_long = math.radians(end[0])
  end_latt = math.radians(end[1])
  d_latt = end_latt - start_latt
  d_long = end_long - start_long
  a = math.sin(d_latt/2)**2 + math.cos(start_latt) * math.cos(end_latt) * math.sin(d_long/2)**2
  c = 2 * math.atan2(math.sqrt(a),  math.sqrt(1-a))
  #the average altitude of the iss is = 405.8 km over the sea
  return (6371+405.8) * c

"""
    If I am running this module as the main program, and I am not calling it 
    from the main, then it can assign two specific values 
    ( instead of getting the two parameters from the main )
"""

if __name__ == '__main__':
    #half earth circumference
 before = (90,0)
 after = (90,180)
 print (points2distance(before, after))
