from django import forms
from testapp.models import Employee
from django.core.exceptions import ValidationError 

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        input_sal = self.cleaned_data['esal']
        if input_sal<5000:
            raise forms.ValidationError("The minimum salary should be 5000")
        return input_sal
    class Meta:
        model = Employee
        fields = '__all__'

