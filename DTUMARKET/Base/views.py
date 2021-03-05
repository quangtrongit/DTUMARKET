from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'base/index.html')


def notification(request):
    return render(request, 'base/notification.html')


def Posts(request):
    return render(request, 'base/Posts.html')


def Profile(request):
    return render(request, 'base/Profile.html')
