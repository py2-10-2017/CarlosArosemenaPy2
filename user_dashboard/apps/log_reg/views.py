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



def render_login(req):
    return render(req, 'log_reg/login.html')

def login(req):
    errors = {}
    checkUserEmail = users.objects.filter(email_address = req.POST['log_email'])
    # hashedPasswordCheck = bcrypt.hashpw(req.POST['log_password'].encode(), bcrypt.gensalt())


    if not checkUserEmail:
        errors['login error'] = "invalid username/password"
    else:
        for user in checkUserEmail:
            # passwordinDB = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
            # print passwordinDB
            # print hashedPasswordCheck
            if  bcrypt.checkpw(req.POST['log_password'].encode(), user.password.encode()):
                req.session['email_address']= user.email_address
                req.session['first_name'] = user.first_name
                req.session['last_name'] =user.last_name
                req.session['what'] = 'logged in'
                return redirect('/register/success')
            else:
                errors['login error'] = "invalid username/password"


    if errors:
        print errors
        for tag, error in errors.iteritems():
            messages.error(req,error, extra_tags=tag)
        return redirect('/login')





def success_registration(req):
    context = {
        'email' : req.session['email_address'],
        'first_name' : req.session['first_name'],
        'last_name' : req.session['last_name'],
        'What' : req.session['what']
    }

    return render(req,'log_reg/registrationsuccess.html', context)


# Create your views here.
