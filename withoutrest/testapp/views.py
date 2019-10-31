from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from django.views.generic import View


# Create your views here.
def emp_data_view(request):
    emp_data = {
        'eno':1,
        'ename':'Sunny',
        'esal':1000,
        'eaddr':'Mumbai'
    }
    # resp = json.dumps(emp_data)
    # return HttpResponse(resp,content_type='application/json')
    return JsonResponse(emp_data)

class jsonCbv(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
        'eno':1,
        'ename':'Sunny',
        'esal':1000,
        'eaddr':'Mumbai'
        }
        return JsonResponse(emp_data)
    



