from testapp.models import Employee
import json

def get_object_id(id):
    try:
        emp = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        emp = None
    return emp


def is_json(data):
    try:
        pdata = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid
