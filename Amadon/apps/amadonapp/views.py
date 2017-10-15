from django.shortcuts import render, HttpResponse, render, redirect
from inventory import inventory


def index(req):
    context =  {
            'items':inventory,
        }

    return render(req, 'amadonapp/index.html',context)

def checkout(req):
    context = {
     'charged': req.session['charge'],
     'totalcharge': req.session['chargeHistory'],
     'ordered': req.session['orderedToDate']
    }

    return render(req, 'amadonapp/checkout.html', context)

def process(req, product_id):

    try:
        req.POST['quantity']

    except KeyError:
        return redirect('/')

    try:
        req.session['charge']
        req.session['ordered']
        req.session['orderedToDate']
        req.session['chargeHistory']
    except KeyError:
        req.session['charge'] = 0
        req.session['ordered'] = 0
        req.session['orderedToDate'] = 0
        req.session['chargeHistory'] = 0


    for product in inventory:
        if product['id'] == int(product_id):
            cccharge = product['price'] * int(req.POST['quantity'])
            ordered = int(req.POST['quantity'])

    req.session['charge'] = cccharge
    req.session['ordered']= ordered
    orderedsofar = req.session['ordered']
    req.session['orderedToDate'] += orderedsofar
    latestcharge = req.session['charge']
    req.session['chargeHistory'] += latestcharge


    return redirect('/amadon/checkout')
# Create your views here.
def reset(req):
    del req.session['charge']
    del req.session['ordered']
    del req.session['orderedToDate']
    del req.session['chargeHistory']

    return redirect('/')
