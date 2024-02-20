from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello there, this is Omusakhulu!")

# Create your views here.
