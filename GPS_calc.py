# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:44:23 2022

@author: wilamowsse01
"""

# import geopy.distance
# # from geopy import distance

# coords_1 = (52.2296756, 21.0122287)
# coords_2 = (52.406374, 16.9251681)

# print distance.distance(coords_1, coords_2).km

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="spyder_test_script")
location = geolocator.geocode("Kolonia Zbyszkow 9C Grabow nad Pilica Poland")
print(location.address)
print((location.latitude, location.longitude))
# print(location.raw)

location = geolocator.reverse("51.73, 21.20")
print(location.address)
print((location.latitude, location.longitude))
# print(location.raw)

from geopy.distance import geodesic
loc1 = (51.7343247, 21.2002061)
loc2 = (51.7, 21.2)
print(geodesic(loc1, loc2).m)

