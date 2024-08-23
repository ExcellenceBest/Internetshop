from django.shortcuts import render
from django.http import HttpRequest

def main(request: HttpRequest):
    return render(request, 'about2.html')

def redirect(request: HttpRequest):
    return render(request, '404.html')