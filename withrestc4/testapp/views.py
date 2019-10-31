from django.shortcuts import render,get_object_or_404
from rest_framework.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views h.ere.

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id !=None:
            emp = Employee.objects.get(id=id)
            eserializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json',status=200)
        emp = Employee.objects.all()
        eserializer = EmployeeSerializer(emp,many=True)
        json_data = JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        eserializer = EmployeeSerializer(data=pdata)
        if eserializer.is_valid():
            eserializer.save()
            msg = {"Resource Created Successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json',status=200)
        json_data = JSONRenderer().render(eserializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=200)

    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        emp1 = Employee.objects.get(id=id)
        emp = EmployeeSerializer(emp1,data=pdata,partial=True)
        if emp.is_valid():
            emp.save()
            msg = {"Resource Updated Successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json',status=200)
        json_data = JSONRenderer().render(emp.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
        
        


