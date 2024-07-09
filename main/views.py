from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest

def main(request: HttpRequest):
    return render(request, 'base.html')

def redirect(request: HttpRequest):
    return render(request, '404.html')
