from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import io
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.pagination import PageNumberPagination
from testapp.pagination import MyPagination
# Create your views here.
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeAPIview(APIView):
#     def get(self,request,*args,**kwargs):
#         id = request.GET.get('id')
#         if id !=None:
#             emp = Employee.objects.get(id=id)
#             eserializer = EmployeeSerializer(emp)
#             # json_data = JSONRenderer().render(eserializer.data)
#             return Response({"result":eserializer.data})
#         emp = Employee.objects.all()
#         eserializer = EmployeeSerializer(emp,many=True)
#         return Response({"result":eserializer.data})

#     def post(self,request,*args,**kwargs):
#         json_data= request.data
#         emp = EmployeeSerializer(data=json_data)
#         if emp.is_valid():
#             emp.save()
#             msg = {"Recource created successfully"}
#             return Response({"result":msg})
#         return Response({"Error":emp.errors})

#     def put(self,request,*args,**kwargs):
#         json_data = request.GET.get('id')
#         data1 = request.data
#         id = json_data
#         emp = Employee.objects.get(id=id)
#         eserializer = EmployeeSerializer(emp,data=data1,partial=True)
#         if eserializer.is_valid():
#             eserializer.save()
#             msg = {"Resource updated Successfuuly"}
#             return Response({"Result":msg})
#         return Response({"Error":eserializer.errors,"status":400})

class EmployeeListApiView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination
    search_fields= ('=eno','ename')
    ordering_fields=('eno','ename')
    # authentication_classes = [JSONWebTokenAuthentication,]
    # permission_classes = [IsAuthenticated,]


