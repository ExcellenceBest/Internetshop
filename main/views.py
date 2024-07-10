from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse

def main(request: HttpRequest):
    return render(request, 'home.html')

def redirect(request: HttpRequest):
    return render(request, '404.html')

def registration(request: HttpRequest):
    return render(request, 'reg.html')
