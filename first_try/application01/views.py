from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(r'Hey man, U can do it')


def Olsen(request):
    return HttpResponse(r' I love Olsen', 'Clarknb.html')


def user(request):
    return HttpResponse(r'User')

def Clarknb(request):
    return render(request, 'Clarknb.html')
