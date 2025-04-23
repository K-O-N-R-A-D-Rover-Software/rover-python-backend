from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle
from geopy import distance

geolocator = Nominatim(user_agent="my_gps_test")
location = geolocator.geocode("Galerieplatz 1, 40764 Langenfeld (Rheinland)")
print(location.address)
print((location.latitude, location.longitude, location.altitude))

location2 = geolocator.geocode("Auf dem Saendchen 24, Langenfeld")
print(location2.address)
print((location2.latitude, location2.longitude, location.altitude))

# Toom Baumarkt
location3 = (51.117465211413354, 6.964970269242966)

print(geodesic((location.latitude, location.longitude), (location2.latitude, location2.longitude)).meters)
print(great_circle((location.latitude, location.longitude), (location2.latitude, location2.longitude)).meters)
print(distance.distance((location.latitude, location.longitude), (location2.latitude, location2.longitude)).meters)
print(distance.distance((location.latitude, location.longitude), location3).meters)