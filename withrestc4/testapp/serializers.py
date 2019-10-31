from testapp.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_esal(self,value):
        if value<5000:
            raise serializers.ValidationError("Salary should be minimum 5000")
        return value
    