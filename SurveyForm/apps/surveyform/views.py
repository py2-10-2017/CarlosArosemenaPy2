from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(req):

    return render(req, 'surveyform/index.html')

def result(req):

    
    context = {
        'name' : req.session['name'],
        'location': req.session['location'],
        'language' : req.session['language'],
        'comment': req.session['comment'],
        'counter': req.session['counter']
    }

    return render(req, 'surveyform/result.html', context)

def process(req):
    req.session['counter'] += 1
    req.session['name'] = req.POST['name']
    req.session['location'] = req.POST['location']
    req.session['language'] = req.POST['language']
    req.session['comment'] = req.POST['comment']

    return redirect('/result')
