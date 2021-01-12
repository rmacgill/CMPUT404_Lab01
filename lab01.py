import requests

#print(requests.__version__)
#print(requests.get("http://www.google.com"))
print(requests.get("https://raw.githubusercontent.com/rmacgill/CMPUT404_Lab01/master/lab01.py").text)
