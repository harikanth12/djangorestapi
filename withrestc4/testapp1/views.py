from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp1.serializers import ExampleSerializer

# Create your views here.
class ExampleAPIVIEW(APIView):
    def get(self,request,*args,**kwargs):
        colors = ["BLUE","WHITE","GREEN"]
        return Response({"msg":"Welecome to New year",'colors':colors})

    def post(self,request,*args,**kwargs):
        # print(data)
        serializer = ExampleSerializer(data=request.data)
        if serializer.is_valid():
            ename = serializer.data.get('ename')
            msg = f"Hello {ename} wish you a Happy New Year"
        return Response({"result":msg})
    def put(self,request):
        return Response({"msg":"This is a Put method"})

    def patch(self,request):
        return Response({"msg":"This is a Patch method"})

    def delete(self,request):
        return Response({"msg":"This is a delete method"})
    

