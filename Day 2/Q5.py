import requests
print("timeout = 0.001")
try: 
   #requesting data from the web page and stop waiting after stated time
    r = requests.get('https://www.ted.com/', timeout = 3.)
    print(r.text)
except requests.exceptions.RequestException as e:
    print(e) 

    #request is timedout incase of failure  
print("\ntimeout is  = 5.0")  

#in the event of failure in the first request
try:
    r = requests.get('https://www.ted.com/', timeout = 10.0)
    print("Connected....!")
except requests.exceptions.RequestException as e:
    print(e)
