from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_kavi(request):
    return HttpResponse('my name is kavireddy')
    