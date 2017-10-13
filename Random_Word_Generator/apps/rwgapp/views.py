from django.shortcuts import render, HttpResponse

def index(req):
    context = {
        "randomWord":"CarlosArosemenaWord"
    }
    return render(req, 'rwgapp/index.html', context)

# Create your views here.
