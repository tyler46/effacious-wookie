import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseBadRequest

import redis

from newspaper.articles.serializers import ArticleSerializer

r = redis.StrictRedis(host='localhost', port=6379, db=0)


@csrf_exempt
@require_POST
def add_article(request):
    """Accepts a request from node.js and creates a new article instance."""

    reporter_id =  int(request.POST.get('reporter'))
    headline = request.POST.get('headline')
    data = {
        'headline': headline,
        'reporter': reporter_id
    }

    serializer = ArticleSerializer(data=data)
    if not serializer.is_valid():
        return HttpResponseBadRequest('Incorrect data')

    serializer.save()
    r.publish('news', serializer.data)

    return HttpResponse('OK')
