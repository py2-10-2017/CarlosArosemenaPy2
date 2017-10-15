from django.shortcuts import render, HttpResponse, render, redirect


def index(req):
    return render(req, 'amadonapp/index.html')

def checkout(req):
    return render(req, 'amadonapp/checkout.html')

def process(req):
    return redirect('/amadon/checkout')
# Create your views here.
