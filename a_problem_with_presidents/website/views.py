from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("This is my homepage!!!")


def date(request):
    return HttpResponse("The time now is: " + str(datetime.now()))