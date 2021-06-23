import requests
import json

#url where data is read from
r = requests.get('https://knh.or.ke/')

#capturing json response in python dictionary

r_dict = r.json()

#access the response

print(r.dict)
