from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# django criado baseado em

# M -> models.py
# T -> template
# V -> views.py


def home(request):
    return HttpResponse("Olá")


def home_param(request, post_id):
    return HttpResponse("Olá: %s" % post_id)