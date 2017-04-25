from django.http import JsonResponse, Http404
from django.shortcuts import render
from djangoApiDec.djangoApiDec import queryString_required, date_proc, queryString_required_ClassVersion
from django.forms.models import model_to_dict
from arrogant.models import *
from django.views import View
from django.core import serializers
import json, datetime

@queryString_required(['school', 'dept', 'degree'])
def recommendJvalue(request):
    try:
        j = Job.objects.all()[0]
        result = model_to_dict(j)
        result['avatar'] = result['avatar'].url if result['avatar'] else None
        result['company'] = j.company.company
        return JsonResponse(result, safe=False)
    except Exception as e:
        raise e

@queryString_required(['id'])
def jvalue(request):
    try:
        j = Job.objects.get(id=request.GET['id'])
        result = model_to_dict(j)
        result['avatar'] = result['avatar'].url if result['avatar'] else None
        result['company'] = j.company.company
        return JsonResponse(result, safe=False)
    except Exception as e:
        raise e

# 這邊應該要改成school當作參數，後端把學校轉成縣市名稱，然後用縣市去查詢該縣市的職缺
@queryString_required(['location', 'start'])
def jlist(request):
    start = int(request.GET['start']) - 1
    result = Job.objects.filter(地區=request.GET['location'])[start:start+15]
    return JsonResponse(json.loads(serializers.serialize('json', list(result))), safe=False)

# 顯示特定一門課程的留言評論
@queryString_required(['id', 'start'])
def comment(request):
    try:
        start = int(request.GET['start']) - 1
        j = Job.objects.get(id=request.GET['id'])
        result = j.comment_set.all()[start:start+15]
        return JsonResponse(json.loads(serializers.serialize('json', list(result))), safe=False)
    except Exception as e:
        print('job not found ' + str(e))
