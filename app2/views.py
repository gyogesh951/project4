from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def abhi(request):
    return HttpResponse('<h1><i>abhi is a loverboy</h1></i>')