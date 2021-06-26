from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

#User Inout
x = int(input("Enter the zipcode:\n"))

#using geolocator.geocode()  to get details of the zipcode
location = geolocator.geocode(x)
print("Details of the said pincode:")
print(location.address)
