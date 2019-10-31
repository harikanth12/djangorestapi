from django.shortcuts import render
from django.views.generic import View
import json
from django.http import HttpResponse
from testapp.models import Employee
from testapp.utils import get_object_id,is_json
from testapp.mixins import HttpResponseMinmix,SerializeMixin
from testapp.forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeCURDCBV(HttpResponseMinmix,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':"Please send the data in json only"})
            return self.get_http_response(json_data,status=400)
        pdata = json.loads(data)
        new_data = pdata.get('id',None)
        if new_data is not None:
            emp = get_object_id(new_data)
            
            if emp is None:
                json_data = json.dumps({'msg':"There is no data matched with this id"})
                return self.get_http_response(json_data,status=400)
            json_data = self.serialize([emp])
            return self.get_http_response(json_data)
        emp = Employee.objects.all()
        json_data = self.serialize(emp)
        return self.get_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please send me the valid Json data only"})
            return self.get_http_response(json_data,status=400)
        pdata = json.loads(data)
        form = EmployeeForm(pdata)
        if form.is_valid():
            form.save()
            json_data = json.dumps({"msg":"Resource created successfully"})
            return self.get_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.get_http_response(json_data)

    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data =json.dumps({"msg":"Please provide the valid Json data only"})
            return self.get_http_response(json_data,status=400)
        pdata = json.loads(data)
        # print(pdata,"data is")
        new_json_data = pdata['id']
        emp = get_object_id(new_json_data)
        if emp is None:
            json_data =json.dumps({"msg":"No data is found with this id,so there is no updation"})
            return self.get_http_response(json_data,status=400)
        orginal_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        orginal_data.update(pdata)
        form = EmployeeForm(orginal_data,instance=emp)
        if form.is_valid():
            form.save()
            json_data =json.dumps({"msg":"Resource updated Successfully"})
            return self.get_http_response(json_data)
        if form.errors:
            json_data =json.dumps(form.errors)
            return self.get_http_response(json_data)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data =json.dumps({"msg":"Please provide the valid Json data only"})
            return self.get_http_response(json_data,status=400)
        pdata = json.loads(data)
        # print(pdata,"data is")
        new_json_data = pdata['id']
        emp = get_object_id(new_json_data)
        if emp is None:
            json_data =json.dumps({"msg":"No data is found with this id,so there is no deletion"})
            return self.get_http_response(json_data,status=400)
        status,deleted_items = emp.delete()
        if status == 1:
            json_data =json.dumps({"msg":"Resource deleted Successfully"})
            return self.get_http_response(json_data)
        json_data =json.dumps({"msg":"There is something problem please try again,.."})
        return self.get_http_response(json_data)

        

    
