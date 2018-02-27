#from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import District

def district_model2dict(district):
    """
    convert a district record to a dict
    """
    return dict(code=district.code, name=district.name, parent=district.parent, level=district.level)

class MyJsonResponse(JsonResponse):
    def __init__(self, data):
        super().__init__(data, json_dumps_params={'ensure_ascii':False}, content_type='application/json;charset=utf-8')

# Create your views here.
@require_GET
def index(request):
    rsp = {'status':0, 'district':[]}
    try:
        districts = District.objects.all()
        data = [district_model2dict(d) for d in districts]
        rsp = dict(status=0, data=data)
    except Exception:
        rsp = dict(status=1, message='Query failure')
    return MyJsonResponse(rsp)

@require_GET
def get_district_info(request, code):
    """
    Get district info by 'code'
    """
    try:
        district = District.objects.get(code=code)
        child_districts = District.objects.filter(parent=district.code)
        data = district_model2dict(district)
        children = [district_model2dict(c) for c in child_districts]
        data.setdefault('children', children)
        rsp = dict(status=0, data=data)
    except Exception:
        rsp = dict(status=1, message='No such district')
    return MyJsonResponse(rsp)
