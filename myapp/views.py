from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# django criado baseado em

# M -> models.py
# T -> template
# V -> views.py


def home(request):
    return HttpResponse("Olá")


def home_param(request, post_id):
    return HttpResponse("Olá: %s" % post_id)


def post_list(request):
    name = "Helder Santos"
    return render(request, "post_list.html", {"name": name})
