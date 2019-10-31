import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsoncbv/'
res = requests.get(BASE_URL+ENDPOINT)
# print(type(res.json()))
data = res.json()
print("Data is coming from Django application")
print('*'*50)
print(f"Employee No:{data['eno']}")
print(f"Employee Name:{data['ename']}")
print(f"Employee Salary:{data['esal']}")
print(f"Employee Address:{data['eaddr']}")
