from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from ..log_reg.models import *

def dashboard(req):
    context = {
        'users' : users.objects.all(),
        'role': req.session['user'],
        'user_in_session' : req.session['email_address']
    }
    return render(req, 'adminapp/dashboard.html', context)

def render_regform(req):
    if req.session['user'] == 9:
        return render(req, 'adminapp/registration.html')
    else:
        return redirect('/dashboard')

def success_registration(req):
    context = {
        'email' : req.session['email_address'],
        'first_name' : req.session['first_name'],
        'last_name' : req.session['last_name'],
        'What' : req.session['what']
    }

    return render(req,'log_reg/registrationsuccess.html', context)


def submit_registration(req):
    errors = users.objects.user_validator(req.POST)


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

        print user.first_name
        req.session['email_address']= user.email_address
        req.session['first_name'] = user.first_name
        req.session['last_name'] =user.last_name
        req.session['what'] = 'registered'


        return redirect('/register/success')


# Create your views here.
