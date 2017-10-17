from django.shortcuts import render, HttpResponse
from queries import Bookstore

# Create your views here.
def index(req):
    for book in Bookstore:
        response = book['name']
    return HttpResponse(response)
