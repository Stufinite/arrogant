from django.http import JsonResponse, Http404
from django.shortcuts import render
from djangoApiDec.djangoApiDec import queryString_required
from django.forms.models import model_to_dict
from arrogant.models import *
from django.views import View
from django.core import serializers
import json, datetime, os
from infernoWeb.view.inferno import user_verify
from django.db.models import F

school2loc = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'school2location.json'), 'r'))
dept2job = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'dept2job.json'), 'r'))
AMOUNT_NUM = 10
SEARCH_NUM = 5

@queryString_required(['dept'])
def recommendJvalue(request):
    import random
    dept = request.GET['dept']
    for i in dept2job:
        if i in dept:
            random.shuffle(dept2job[i])
            jid = Category.objects.get(name=dept2job[i][0]).job_set.random().id
            request.GET = request.GET.copy()
            request.GET['id'] = jid
            return jvalue(request)
    return JsonResponse({}, safe=False)

@queryString_required(['id'])
def jvalue(request):
    j = Job.objects.prefetch_related('jobtag_set', 'category', 'skilltag_set', 'company').get(id=request.GET['id'])
    result = model_to_dict(j, exclude='attendee')
    result['company'] = j.company.natural_key()
    result['JobTag'] = list(j.jobtag_set.all().values())
    result['skilltag'] = list(j.skilltag_set.all().values())
    result['Category'] = j.category.name
    return JsonResponse(result, safe=False)

@queryString_required(['start'])
def jlist(request):
    start = int(request.GET['start']) - 1
    category = request.GET['category'] if 'category' in request.GET else "行銷/社群經營"
    querySet = Category.objects.get(name=category).job_set.select_related('company').prefetch_related('jobtag_set', 'category', 'skilltag_set').all()
    length = len(querySet) // AMOUNT_NUM +1

    result = []
    querySet = querySet[start:start+AMOUNT_NUM]
    for i in querySet:
        tmp = model_to_dict(i, exclude='attendee')
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
@user_verify
def CreateComment(request):
    id = request.GET['id']
    j = Job.objects.prefetch_related('comment_set').get(id=id)
    if len(j.comment_set.all().filter(author=User.objects.get(facebookid=request.POST['id'])))==0:
        Comment.objects.create(Job=j, author=User.objects.get(facebookid=request.POST['id']) , create=timezone.now(), raw=request.POST['comments'], emotion=request.POST['emotion'])
        return True
    return False

def logPage(request):
    PageLog.objects.create(user=User.objects.get(facebookid=request.POST['id']), Job=Job.objects.get(id=request.GET['id']), create=timezone.now())

@queryString_required(['id'])
@user_verify
def like(request):
    request.GET = request.GET.copy()
    request.GET['start'] = 1
    if request.POST:
        user = User.objects.get(facebookid=request.POST['id'])
        if request.POST['like'] == '1':
            target = Comment.objects.filter(id=request.GET['id'])
            target.update(like=F('like') + int(request.POST['like']))
            obj, created = LikesFromUser.objects.get_or_create(author=user)
            obj.comment.add(target[0])
            return JsonResponse({"like":'success'})
        elif request.POST['like'] == '-1':
            Comment.objects.filter(id=request.GET['id']).update(like=F('like') + int(request.POST['like']))
            LikesFromUser.objects.get(author=user).comment.remove(Comment.objects.get(id=request.GET['id']))
            return JsonResponse({"like":'success'})

@user_verify
@queryString_required(['id'])
def questionnaire(request):
    id = request.GET['id']
    j = Job.objects.get(id=id)
    if request.method == 'POST' and request.POST:
        if User.objects.get(facebookid=request.POST['id']) in j.attendee.all():
            return JsonResponse({'alreadySubmit':True})
        if 'rating' in request.POST:
            data = json.loads(request.POST['rating'])
            amount = j.feedback_amount + 1
            modelDict = {'feedback_amount':amount}
            modelDict['feedback_freedom'] = (j.feedback_freedom*(amount-1) + (data[0]*3/4 + data[1]/4)) /amount
            modelDict['feedback_salary'] = (j.feedback_salary*(amount-1) + data[2]) / amount
            modelDict['feedback_easy'] = (j.feedback_easy*(amount-1) + (data[3]/12 + data[4]/12  + data[7]*9/12 + data[8]/12)) / amount
            modelDict['feedback_knowledgeable'] = (j.feedback_knowledgeable*(amount-1) + data[6]) / amount
            modelDict['feedback_FU'] = (j.feedback_FU*(amount-1) + data[5]) / amount
            Job.objects.update_or_create(id=id, defaults=modelDict)
            Job.objects.get(id=id).attendee.add(User.objects.get(facebookid=request.POST['id']))
            return JsonResponse({'submitSuccess':True})