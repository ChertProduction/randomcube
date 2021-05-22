from django.shortcuts import render

import logging
from json import dumps, loads
from django.shortcuts import render
from django.template import RequestContext

from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.http import HttpRequest
import redis
from django.conf import settings
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

def index(request):
    return render(request, 'index.html', {
        'foo': 'bar',
    })

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
 
 
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



#class ContactView(APIView):