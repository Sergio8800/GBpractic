from django.shortcuts import render

from django.http import HttpResponse


def index_app(request):
    return HttpResponse("<h1> Hello, world!</h1>")


def about(request):
    return HttpResponse("<h1>About company</h1>")
