from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
import datetime

def activity_finder(request):
    return render(request, 'index.html', {})