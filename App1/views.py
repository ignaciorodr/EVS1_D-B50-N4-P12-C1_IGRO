from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    return HttpResponse("<h1> Primera aplicacion </h1>")


def displayDateTime(request):
    dt=datetime.datetime.now()
    s= "<b>Fecha y hora actual : </b>" + str (dt)
    return HttpResponse(s)


