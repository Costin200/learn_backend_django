from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest


def welcome(request):
    return HttpRequest('Welcome to coding yourself')
