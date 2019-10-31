import requests
import json

BASE_URL= 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id=None):
    edata = {}
    if id is not None:
        edata = {
            'id':id
        }
    print(edata)
    res = requests.get(BASE_URL+ENDPOINT,data=json.dumps(edata))
    print(res.status_code)
    print(res.json())

def create_resource():
    edata = {
        'eno':500,
        'ename':"Bhujjiii",
        'esal':3000,
        'eaddr':'Vskp'
    }
    res = requests.post(BASE_URL+ENDPOINT,data=json.dumps(edata))
    print(res.status_code)
    print(res.json())
# get_resource(1)
def update_resource(id=None):
    edata = {
        'id':id,
        'ename':"jannu",
        'esal':10000,
        'eaddr':'Vskp'
    }
    res = requests.put(BASE_URL+ENDPOINT,data=json.dumps(edata))
    print(res.status_code)
    print(res.json())
# create_resource()
update_resource(5)



