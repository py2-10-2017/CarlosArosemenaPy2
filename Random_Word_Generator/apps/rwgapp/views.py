from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(req):
    try:
        req.session['counter']
        req.session['randomWord']

    except KeyError:
        req.session['counter'] = 0
        req.session['randomWord'] = 'Please click "Generate" to get display a random word"'

    context = {
        'counter':req.session['counter'],
        'randomWord':req.session['randomWord']
    }
    # req.session['randomWord'] = "Click 'Generate' to display a random word"
    return render(req, 'rwgapp/index.html', context)

def generate(req):
    randomness = get_random_string(length=14)
    print randomness
    req.session['randomWord'] = randomness
    req.session['counter'] += 1
    print req.session['counter']
    print req.session['randomWord']
    return redirect('/')

def reset(req):
    del req.session['counter']
    del req.session['randomWord']
    return redirect('/')
