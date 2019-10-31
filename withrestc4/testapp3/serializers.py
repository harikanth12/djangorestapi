from rest_framework import serializers
from testapp3.models import Employee

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
    