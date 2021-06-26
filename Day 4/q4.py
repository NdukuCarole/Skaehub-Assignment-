from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")


#User input of state name
x= input("Enter your state name: ")

print("State Name:",x)

#output of the country name
location = geolocator.geocode(x)
print("State Name/Country Name: ")
print(location.address)


