import requests

#sending request to the web page
response = requests.get('https://www.jhu.edu/')
print("Response text of https://www.jhu.edu/:")


#if success full print response in text
print(response.text)
print("\n==============================================================================")


#once the response is gotten print raw data of the URL
print("\nContent of the said url:")
print(response.content)
print("\n==============================================================================")


#gzip encoding of the output
print("\nRaw data of the said url:")
r = requests.get('https://www.jhu.edu/', stream = True)
print(r.raw)
print(r.raw.read(15))

#check whether the request is OK
print(response)
print(response.status_code)
