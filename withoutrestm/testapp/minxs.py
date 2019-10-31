from django.core.serializers import serialize
import json
from django.http import HttpResponse



class SeralizeMinix:
    def serialize(self,qs):
        json_data = serialize('json',qs)  #list of query set we have to pass.... json_data return json datatype
        pdict = json.loads(json_data) ## json converts into python dict
        final_list = []
        for obj in pdict:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)  ### converting python dict to json
        return json_data

