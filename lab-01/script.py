import requests

print("requests version = " + requests.__version__)
print("GET http://www.google.com/ =", requests.get("http://www.google.com/"))