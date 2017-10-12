from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    response = "Django App Assignment"
    return HttpResponse(response)
