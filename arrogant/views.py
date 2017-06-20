from django.http import JsonResponse, Http404
from django.shortcuts import render
from djangoApiDec.djangoApiDec import queryString_required, date_proc, queryString_required_ClassVersion
from django.forms.models import model_to_dict
from arrogant.models import *
from django.views import View
from django.core import serializers
import json, datetime

school2loc = json.load(open('arrogant/school2location.json', 'r'))
AMOUNT_NUM = 10
SEARCH_NUM = 5

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
    j = Job.objects.get(id=request.GET['id'])
    result = model_to_dict(j)
    return JsonResponse(result, safe=False)

@queryString_required(['school', 'start'])
def jlist(request):
    start = int(request.GET['start']) - 1
    category = request.GET['category'] if 'category' in request.GET else "行銷/社群經營"

    location = list(filter(lambda x:x['abbreviation']==request.GET['school'], school2loc))[0]['location']
    querySet = Category.objects.get(name=category).Job.select_related('company').prefetch_related('jobtag_set', 'category_set', 'skilltag_set').filter(company__area=location)
    length = len(querySet) // AMOUNT_NUM +1

    result = []
    for i in querySet:
        tmp = model_to_dict(i)
        tmp['company'] = i.company.natural_key()
        tmp['jobtag'] = [tag.name for tag in i.jobtag_set.all()]
        tmp['skilltag'] = [(tag.name, tag.skill_field) for tag in i.skilltag_set.all()]
        result.append(tmp)

    querySet = querySet[start:start+AMOUNT_NUM]
    return JsonResponse([{'TotalPage':length, 'school':request.GET['school'], 'category':category}] + result, safe=False)

def jcategory(request):
    return JsonResponse(json.loads(serializers.serialize('json', Category.objects.all(), fields=('name'))), safe=False)

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
