from django.http import JsonResponse, Http404
from djangoApiDec.djangoApiDec import queryString_required, date_proc, queryString_required_ClassVersion
from django.forms.models import model_to_dict
from arrogant.models import *
from django.views import View
import json

@queryString_required(['school', 'dept'])
def jvalue(request):
    try:
        j = Job.objects.all()[0]
        result = model_to_dict(j)
        result['avatar'] = result['avatar'].url if result['avatar'] else None
        result['company'] = j.company.company
        return JsonResponse(result, safe=False)
    except Exception as e:
        raise e