from django.http import JsonResponse, Http404
from django.shortcuts import render
from djangoApiDec.djangoApiDec import queryString_required
from django.forms.models import model_to_dict
from arrogant.models import *
from django.views import View
from django.core import serializers
import json, datetime
from infernoWeb.view.inferno import user_verify

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
    j = Job.objects.prefetch_related('jobtag_set', 'category_set', 'skilltag_set', 'company').get(id=request.GET['id'])
    result = model_to_dict(j)
    result['company'] = j.company.natural_key()
    result['JobTag'] = list(j.jobtag_set.all().values())
    result['skilltag'] = list(j.skilltag_set.all().values())
    result['Category'] = j.category_set.all().values()[0]
    return JsonResponse(result, safe=False)

@queryString_required(['start'])
def jlist(request):
    start = int(request.GET['start']) - 1
    category = request.GET['category'] if 'category' in request.GET else "行銷/社群經營"

    # location = list(filter(lambda x:x['abbreviation']==request.GET['school'], school2loc))[0]['location']
    querySet = Category.objects.get(name=category).Job.select_related('company').prefetch_related('jobtag_set', 'category_set', 'skilltag_set').all()
    # querySet = Category.objects.get(name=category).Job.select_related('company').prefetch_related('jobtag_set', 'category_set', 'skilltag_set').filter(company__area=location)
    length = len(querySet) // AMOUNT_NUM +1

    result = []
    querySet = querySet[start:start+AMOUNT_NUM]
    for i in querySet:
        tmp = model_to_dict(i)
        tmp['company'] = i.company.natural_key()
        tmp['jobtag'] = [tag.name for tag in i.jobtag_set.all()]
        tmp['skilltag'] = [(tag.name, tag.skill_field) for tag in i.skilltag_set.all()]
        result.append(tmp)

    return JsonResponse([{'TotalPage':length, 'category':category}] + result, safe=False)

def jcategory(request):
    return JsonResponse(json.loads(serializers.serialize('json', Category.objects.all(), fields=('name'))), safe=False)

# 顯示特定一門課程的留言評論
@queryString_required(['id', 'start'])
def comment(request):
    try:
        start = int(request.GET['start']) - 1
        j = Job.objects.prefetch_related('comment_set').get(id=request.GET['id'])
        comments = j.comment_set.all()[start:start+AMOUNT_NUM]

        result = []
        for i, j in zip(json.loads(serializers.serialize('json', comments, use_natural_foreign_keys=True, use_natural_primary_keys=True)), comments):
            i['fields']['likesfromuser'] = list(map(lambda x:x.author.facebookid, j.likesfromuser_set.all()))
            result.append(i)

        return JsonResponse(result, safe=False)
    except Exception as e:
        raise


# 建立特定一門課程的留言評論
@queryString_required(['id'])
# @user_verify
def CreateComment(request):
    id = request.GET['id']
    j = Job.objects.prefetch_related('comment_set').get(id=id)
    if len(j.comment_set.all().filter(author=User.objects.get(facebookid=request.POST['id'])))==0:
        Comment.objects.create(Job=j, author=User.objects.get(facebookid=request.POST['id']) , create=timezone.now(), raw=request.POST['comments'], emotion=request.POST['emotion'])
        return True
    return False

def logPage(request):
    PageLog.objects.create(user=User.objects.get(facebookid=request.POST['id']), Job=Job.objects.get(id=request.GET['id']), create=timezone.now())