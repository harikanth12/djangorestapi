from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeView(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        print(pdata)
        id_exits = pdata.get('id',None)
        if id_exits !=None:
            emp = Employee.objects.get(id=id_exits)
            eserializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json',status=200)
        qs = Employee.objects.all()
        eserializer = EmployeeSerializer(qs,many=True)
        json_data = JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data,content_type='application/json',status=200)

    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pdata)

        if serializer.is_valid():
            serializer.save()
            msg = {" Resource Created Successfully "}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json',status=200)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)

    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        eserializer = EmployeeSerializer(emp,data=pdata,partial=True)
        if eserializer.is_valid():
            eserializer.save()
            msg = {"Resource Updated Successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json',status=200)
        json_data = JSONRenderer().render(eserializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)





