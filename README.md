import requests
import json, pdb

class Api:
    URL = "https://reqres.in/api/users/2"
    response = requests.get(URL)
    data1 = response.json()
    print(data1)
