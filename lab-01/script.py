import requests

print("requests version = " + requests.__version__)
print('requests.get("http://www.google.com/") =', requests.get("http://www.google.com/"))
python_request = requests.get("https://raw.githubusercontent.com/aaronskiba/CMPUT-404/main/lab-01/script.py")
print("python script:\n", python_request.text)