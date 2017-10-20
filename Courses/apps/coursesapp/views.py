from django.shortcuts import render, HttpResponse


def index(req):

    return render(req,'coursesapp/index.html')

def delete(req):

    return render(req,'coursesapp/destroy.html')
# Create your views here.
