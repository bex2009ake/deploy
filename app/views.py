from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_res(res):
    return HttpResponse('<h1>Hello, GitHub</h1>')