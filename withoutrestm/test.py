import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT='apijson/'

def get_empdetails(id):
    res = requests.get(BASE_URL+ENDPOINT+id+'/')
    json_data = res.json()
    print(json_data)

def get_emplistdata():
    res = requests.get(BASE_URL+ENDPOINT)
    json_data = res.json()
    print(json_data)

def create_resource():
    new_data = {
        'eno':600,
        'ename':"Mallika",
        'esal':3000,
        'eaddr':"Mumbai"
    }
    res = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(res.status_code)
    print(res.json())

def update_resource(id):
    new_data = {
        'esal':7000,
        'eaddr':'Chennai'
    }
    res = requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_data))
    print(res.status_code)
    print(res.json())

def delete_resource(id):
    res = requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
    print(res.status_code)
    print(res.json())

delete_resource(6)