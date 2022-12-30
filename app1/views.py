from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dani(request):
    return HttpResponse('<h1><marque>dani is best actor</h1></marque>')
def yogi(request):
    return HttpResponse('yogi is a badboy')