import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id=None):
    edata = {}
    if id !=None:
        edata ={
            'id':id
        }
    print(edata)
    res = requests.get(BASE_URL+ENDPOINT,data=json.dumps(edata))
    print(res.status_code)
    print(res.json())

def create_resource():
    edata = {
        'eno':5,
        'ename':'Bhujii',
        'esal':'bbbfbvb',
        'eaddr':'Kavali'
    }
    res = requests.post(BASE_URL+ENDPOINT,data=json.dumps(edata))
    print(res.status_code)
    print(res.json())

def update_resource(id=None):
    edata = {
        'id':id,
        'ename':"Jannu",
        'esal':100
    }
    res = requests.put(BASE_URL+ENDPOINT,data=json.dumps(edata))
    print(res.status_code)
    print(res.json())


update_resource(6)



    
    
