from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return HttpResponse('Hello there')

def my_first_project(request):
  return render(request, 'my_first_project/files.html', {'data': 'test-data'})