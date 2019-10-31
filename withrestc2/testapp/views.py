from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializer import EmployeeSerializer
from rest_framework.response import Response

# Create your views here.
class EmployeeAPIVIEW(APIView):
    def get(self,request,format=None,*args,**kwargs):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            eno = serializer.data.get
        





