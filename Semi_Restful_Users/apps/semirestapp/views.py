from django.shortcuts import render, redirect
from models import restuser
from django.contrib import messages
from django.db import IntegrityError


def index(req):

    allusers = restuser.objects.all()

    context = {
        "allusers" : allusers
    }

    return render(req, 'semirestapp/index.html', context)

# Create your views here.
def show(req, user_id):
    usertoDisplay = restuser.objects.get(id=user_id)

    context = {
        "usertoDisplay":usertoDisplay
    }
    return render(req, 'semirestapp/show.html',context)

def new(req):
    return render(req, 'semirestapp/create.html')

def create(req):
    errors = restuser.objects.user_validator(req.POST)

    if errors:
        for tag, error in errors.iteritems():
            messages.error(req, error,extra_tags=tag)
        return redirect('/users/new')

    else:
        newuser = restuser.objects.create(first_name=req.POST['first_name'],last_name=req.POST['last_name'],email_address=req.POST['email_address'])

    return redirect('/users')

def edit(req, user_id):
    context = {
        'user': restuser.objects.get(id=user_id)
    }
    return render(req, 'semirestapp/edit.html', context)

def update(req, user_id):
    errors = restuser.objects.update_user_validator(req.POST)

    if errors:
        for tag, error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)

        return redirect('/users/{}/edit'.format(user_id))
    else:
        usertoUpdate = restuser.objects.get(id=user_id)
        usertoUpdate.first_name = req.POST['first_name']
        usertoUpdate.last_name = req.POST['last_name']
        usertoUpdate.email_address = req.POST['email_address'] #how to handle IntegrityError at /users/1/update???

        usertoUpdate.save()

        return redirect('/')

def delete(req, user_id):
    usertoDelete = restuser.objects.get(id=user_id)

    usertoDelete.delete()

    return redirect('/')
