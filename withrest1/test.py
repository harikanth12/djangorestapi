import requests
import json

BASEPOINT = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    res = requests.get(BASEPOINT+ENDPOINT,data=json.dumps(data))
    print(res.status_code)
    print(res.json())

def create_resource():
    new_data = {
        'eno':400,
        'ename':"Shiva",
        'esal':4000,
        'eaddr':"Ranchi"
    }
    res = requests.post(BASEPOINT+ENDPOINT,data=json.dumps(new_data))
    print(res.status_code)
    print(res.json())

create_resource()
