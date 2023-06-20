from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index (res):
    return render(res, 'main/index.html')