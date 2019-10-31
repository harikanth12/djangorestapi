from django.http import HttpResponse
from django.core.serializers import serialize
import json

class HttpResponseMinmix:
    def get_http_response(self,json_data,status=None):
        return HttpResponse(json_data,content_type='application/json',status=status)

class SerializeMixin:
    def serialize(self,qs):
        json_data = serialize('json',qs)
        pdata = json.loads(json_data)
        final_list = []
        for obj in pdata:
            emp_data = obj['fields']
            final_list.append(emp_data)
        final_json_data = json.dumps(final_list)
        return final_json_data
         