from geopy.geocoders import Nominatim
geolocate = Nominatim(user_agent="distance_calc")

# User Input
longitude = str(input("enter longitude"))
latitude = str(input("enter latitude"))
locates=latitude+","+longitude
#Get location
#"52.509669-la, 13.376294-lo"
location = geolocate.reverse(locates)
print(location.address)
print((location.latitude, location.longitude))


