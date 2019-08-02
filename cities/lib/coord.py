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

def recalculate_coordinate(val,  _as=None):
  """
    Accepts a coordinate as a tuple (degree, minutes, seconds)
    You can give only one of them (e.g. only minutes) as a floating point 
    number and it will be duly recalculated into degrees, minutes OR seconds.
    Return value can be specified as 'deg', 'min' or 'sec'; default return 
    value is a proper coordinate tuple.  
    
    FOR THE 'DEG' CASE WE DON'T NEED ALL THOSE CALCULATIONS SINCE WE SUM UP EVERYTHING IN SEC.
    BUT THOSE ARE VERY USEFUL FOR THE PROPER TUPLE IN THE DEFAULT CASE (this 
    is not used in our program, since we always call the method
    as (variable, 'deg') but it could be reused in other programs)
  """
  deg,  min,  sec = val
  # pass outstanding values from right to left (in order to have only values in (0,60))
  min = (min or 0) + int(sec) / 60
  sec = sec % 60
  deg = (deg or 0) + int(min) / 60
  min = min % 60
  # pass decimal part from left to right
  dfrac,  dint = math.modf(deg)
  min = min + dfrac * 60
  deg = dint
  mfrac,  mint = math.modf(min)
  sec = sec + mfrac * 60
  min = mint
  if _as:
    sec = sec + min * 60 + deg * 3600
    if _as == 'sec': return sec
    if _as == 'min': return sec / 60
    if _as == 'deg': return sec / 3600
  return deg,  min,  sec
      


def points2distance(start,  end):
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
  start_long = math.radians(recalculate_coordinate(start[0],  'deg'))
  start_latt = math.radians(recalculate_coordinate(start[1],  'deg'))
  end_long = math.radians(recalculate_coordinate(end[0],  'deg'))
  end_latt = math.radians(recalculate_coordinate(end[1],  'deg'))
  d_latt = end_latt - start_latt
  d_long = end_long - start_long
  a = math.sin(d_latt/2)**2 + math.cos(start_latt) * math.cos(end_latt) * math.sin(d_long/2)**2
  c = 2 * math.atan2(math.sqrt(a),  math.sqrt(1-a))
  return 6371 * c

"""
    If I am running this module as the main program, and I am not calling it 
    from the main, then it can assign two specific values 
    ( instead of getting the two parameters from the main )
"""

if __name__ == '__main__':
 warsaw = ((21,  0,  30),  (52, 13, 56))
 cracow = ((19, 56, 18),  (50, 3, 41))
 print (points2distance(warsaw, cracow))
