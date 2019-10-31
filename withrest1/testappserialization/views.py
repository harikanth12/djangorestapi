from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testappserialization.models import Employee
from rest_framework.renderers import JSONRenderer
from testappserialization.serializers import EmployeeSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCURDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            print(serializer.data)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"Resource created successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/data')
        if serializer.errors:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/data')







