from django.shortcuts import render

from json import loads, dumps
from django.http import JsonResponse
from django.template import Context, Template

import json

from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UserCreateForm 
from api.serializers import RandomResponseSerializer, RandomRequestSerializer, ResultsSerializer
from api.utils import Random


from django.http import HttpResponseRedirect

from api.models import Results

from django.template.loader import render_to_string

from django.urls import reverse_lazy
from django.views import generic

from rest_framework.request import Request
from rest_framework.response import Response

from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

import redis
import logging
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
logger = logging.getLogger('django')
redis_access = redis.Redis('localhost', port=6379, db=15)
redis_access.ttl(CACHE_TTL)

def index(request):
    
    results = Results.objects.order_by('-number')

    context = {
        'results': results
    }

#    if request.is_ajax():
#        data = {'rendered_table': render_to_string('index.html', context=context)}
#        return JsonResponse(data)

    return render(request, 'index.html',  context)

class ExampleView(APIView):

    def get(self, request: Request):
        parsed_request = request.query_params.get('number', None)
        print(parsed_request)
        user = request.user.username
        if parsed_request is None:
            return Response(status=400)

        if parsed_request == "1":
            random_number = Random.random()

            print(user)

            model = Results()
            model.number =  random_number
            model.name = user
            model.save()

            response_data = dumps(random_number)

            redis_access.set(random_number, dumps(random_number))                    
        
            response = Response(response_data)
            
            return response
        
        if parsed_request == "2":
            cached = []
            for key in redis_access.keys("*"):
                print(redis_access.get(key))  
                cached.append(redis_access.get(key))

                logger.info(f'Got record  from redis')

            response = Response(cached)

            print(cached)

            return response
        

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
