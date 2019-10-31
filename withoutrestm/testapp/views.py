from django.shortcuts import render
from django.views.generic import View
import json
from django.http import HttpResponse
from testapp.models import Employee
from django.core.serializers import serialize
from testapp.minxs import SeralizeMinix
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utilis import is_json,get_object_id
from testapp.forms import EmployeeForm
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class EmployeedetailCBV(SeralizeMinix,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({"msg":'There is no required data'})
        else:

        # emp_data ={
        #     'eno':emp.eno,
        #     'ename':emp.ename,
        #     'esal':emp.esal,
        #     'eaddr':emp.eaddr
        # }
        # json_data = json.dumps(emp_data)
            json_data = self.serialize([emp])
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,id,*args,**kwargs):
        emp = get_object_id(id)
        if emp is None:
            json_data = json.dumps({"msg":"No Matched records found,so there is no possible to updation"})
            return HttpResponse(json_data,content_type='application/json',status=400)
        data = request.body
        valid_jsondata = is_json(data)
        if not valid_jsondata:
            json_data = json.dumps({"msg":"Please provide the valid json data only "})
            return HttpResponse(json_data,content_type='application/json',status=400)
        provided_data = json.loads(data)
        orginal_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        orginal_data.update(provided_data)
        form = EmployeeForm(orginal_data,instance=emp)
        if form.is_valid():
            form.save()
            json_data = json.dumps({"msg":"Resource created successfully"})
            return HttpResponse(json_data,content_type='application/json')
        if form.errors:
            json_data = json.dumps(form.errors) #form.errors is already in dict format so we create dict again 
            return HttpResponse(json_data,content_type='application/json',status=400)

    def delete(self,request,id,*args,**kwargs):
        emp = get_object_id(id)
        if emp is None:
            json_data = json.dumps({"msg":"No Matched records found,so there is no possible to delete"})
            return HttpResponse(json_data,content_type='application/json',status=400)
        status,deleted_items = emp.delete() ##emp.delete() object returns the tuple data type (status,deleted obkject)
        if status == 1:
            json_data = json.dumps({"msg":"Resource deleted Successfully"})
            return HttpResponse(json_data,content_type='application/json')
        json_data = json.dumps({"msg":"There is something problem...plz try again later"})
        return HttpResponse(json_data,content_type='application/json',status=500)



@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(SeralizeMinix,View):
    def get(self,request,*args,**kwargs):
        emp = Employee.objects.all()
        
        # json_data = serialize('json',emp,fields=('eno','ename'))
        # pdict = json.loads(json_data)
        # final_list = []
        # print(json_data,"empdetails")
        # for obj in pdict:
        #     emp_data = obj['fields']
        #     final_list.append(emp_data)
        # json_data = json.dumps(final_list)
        json_data = self.serialize(emp)

        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please provide the valid json data only "})
            return HttpResponse(json_data,content_type='application/json',status=400)
        emp_data = json.loads(data)
        form =EmployeeForm(emp_data)
        if form.is_valid():
            form.save()
            json_data = json.dumps({"msg":"Resource Updated successfully"})
            return HttpResponse(json_data,content_type='application/json')
        if form.errors:
            json_data = json.dumps(form.errors) #form.errors is already in dict format so we create dict again 
            return HttpResponse(json_data,content_type='application/json',status=400)

