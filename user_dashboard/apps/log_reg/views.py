from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import bcrypt

def index(req):
    return render(req, 'log_reg/index.html')

def register(req):
    return render(req, 'log_reg/registration.html')


def submit_registration(req):
    errors = users.objects.user_validator(req.POST)

    print errors

    if errors:
        for tag,error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/register')

    else:

        hashedPassword = bcrypt.hashpw(req.POST['reg_password'].encode(), bcrypt.gensalt())
        #Make first user admin

        checkUserAdmin = users.objects.all()
        role = 0

        if len(checkUserAdmin) == 0:
            role = 9
        else:
            role = 1

        user = users.objects.create(first_name=req.POST['reg_first_name'],last_name=req.POST['reg_last_name'],email_address=req.POST['reg_email'],password=hashedPassword, user_role = role)


        user.save()

        return redirect('/register/success')



def success_registration(req):

    return render(req,'log_reg/registrationsuccess.html')


# Create your views here.
