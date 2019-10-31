from rest_framework import serializers
from testappserialization.models import Employee

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField()
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)