from django.shortcuts import render
from rest_framework import generics
from testapp3.models import Employee
from testapp3.serializers import ExampleSerializer
# Create your views here.
# class ExampleListapiView(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer
    
# class ExampleListapiView(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename')
#         if name is not None:
#             qs = qs.filter(ename__icontains=name)
#         return qs

# class ExampleCreateView(generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer

# class ExampleRetrieveView(generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer

# class ExampleupdateView(generics.UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer

# class ExampledeleteView(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer

# class ExampleListcreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer

# class ExampleRetrieveUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer

# class ExampleRetrieveDestoryView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = ExampleSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = ExampleSerializer

class EmployeeRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = ExampleSerializer






    
