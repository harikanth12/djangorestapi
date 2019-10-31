from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from testapp2.serializers import ExampleSerializer

# Create your views here.
class ExampleViewsets(viewsets.ViewSet):
    def list(self,request):
        colors = ["Blue","White","Green"]
        return Response(colors)
    def create(self,request):
        serailizer = ExampleSerializer(data=request.data)
        if serailizer.is_valid():
            ename = serailizer.data.get('ename')
            msg = f"Hello {ename} wish you a Happy New Year!!!"
            return Response(msg)
        return Response(serailizer.errors)
    
    def retrieve(self,request):
        return Response({"msg":"This is a retrive method"})

    def update(self,request,pk=None):
        return Response({"msg":"This is a update method"})
        
    
    def destroy(self,request):
        return Response({"msg":"This is a delete method"})

    def partial_update(self,request):
        return Response({"msg":"This is a partial upadte method"})

