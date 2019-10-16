import requests
import json
import jsonpath

class test_fetch_existing_data:
    URL = "https://reqres.in/api/users/2"
    response = requests.get( URL )
    data1 = response.json()
    print("fetching data : ", data1)
    print(response.status_code)

class add_new_data:
    url = "https://reqres.in/api/users/"
    file = open("C:\\Users\\tejal.p\\Downloads\\api\\createuser.json")
    input_json = file.read()
    request_json = json.loads(input_json)
    print("request given is :  ", request_json)
    response = requests.post(url,request_json)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    print("response given is :", response_json)
    id = jsonpath.jsonpath(response_json,'id')
    print("ID is :", id[0])

class update_existing_data:
    link = "https://reqres.in/api/users/2"
    file1 = open("C:\\Users\\tejal.p\\Downloads\\api\\update.json")
    json_input = file1.read()
    request_json1 = json.loads(json_input)
    print("updated data is :" , request_json1)
    response1 = requests.put(link,request_json1)
    response1_json = json.loads(response1.text)
    print("Updated respinse is : ", response1_json)
    up = jsonpath.jsonpath(response1_json, 'updatedAt')
    print("Updated time is : ", up[0])
