import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    # print(data)
    res = requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(res.status_code)
    print(res.json())

def create_resource():
    new_data ={
        'eno':500,
        'ename':"Mallika",
        'esal':5000,
        'eaddr':"Mumbai"
     }
    res = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(res.status_code)
    print(res.json())

def update_resource(id):
    new_data ={
        'id':id,
        'esal':7000,
        'eaddr':"Chennai"
     }
    res = requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(res.status_code)
    print(res.json())

def delete_resource(id):
    data = {
        'id':id
    }
    res = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(res.status_code)
    print(res.json())


delete_resource(5)

