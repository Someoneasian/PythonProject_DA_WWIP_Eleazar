import requests

# To display the header as mobile
headers = {'User-Agent' : 'Mobile'}

# The URL/IP address of my Webserver
url = "http://192.168.1.3/spicyx/"

# Getting the url, then print the status code of the system (Status code of 200 means ok)
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t*", r.status_code)

# Getting the head to get additional information with a request
h = requests.head(url)
print("Header:")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("******")

url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)
