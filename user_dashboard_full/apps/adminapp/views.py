from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from ..log_reg.models import *
from models import *
from django.contrib import messages
import bcrypt


def dashboardadmin(req):
    if req.session['user'] == 9:
        context = {
            'users' : users.objects.all(),
            'role': req.session['user'],
            'user_in_session' : req.session['email_address']
        }
        return render(req, 'adminapp/dashboard.html', context)
    else:
        return redirect('/dashboard')

def dashboard(req):
    if req.session['user'] != 9:
        context = {
            'users' : users.objects.all(),
            'role': req.session['user'],
            'user_in_session' : req.session['email_address']
        }
        return render(req, 'adminapp/dashboard.html', context)
    else:
        return redirect('/dashboard/admin')

def render_regform(req):
    if req.session['user'] == 9:
        context = {
            'user_in_session':req.session['email_address']
        }

        return render(req, 'adminapp/registration.html',context)
    else:
        return redirect('/dashboard')



def submit_new_user(req):

    errors = users.objects.user_validator(req.POST)

    if errors:
        for tag,error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/users/new')

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

        return redirect('/dashboard/admin')

def render_edit(req):
    context = {
        'user_in_session':req.session['email_address'],
        'email':req.session['email_address'],
        'first_name':req.session['first_name'],
        'last_name':req.session['last_name'],
        'user_id': req.session['edit_id']
    }
    return render(req,'adminapp/edit.html', context)

def render_single_edit(req, user_id):
    userToEdit = users.objects.get(id=user_id)
    context = {
        'user_in_session':req.session['email_address'],
        'email':userToEdit.email_address,
        'first_name':userToEdit.first_name,
        'last_name':userToEdit.last_name,
        'user_id': userToEdit.id,
        'role' : req.session['user'],
        'user_role': userToEdit.user_role,
        'description': userToEdit.description
    }
    return render(req,'adminapp/edit.html', context)


def edit_single_submit(req,user_id):
    errors = users.objects.update_user_validator(req.POST)

    if errors:
        for tag,error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/users/edit/{}'.format(user_id))

    else:
        userToUpdate = users.objects.get(id=req.POST['edit_id'])
        userToUpdate.first_name = req.POST['edit_first_name']
        userToUpdate.last_name = req.POST['edit_last_name']
        userToUpdate.email_address = req.POST['edit_email']
        # req.session['email_address'] = req.POST['edit_email']
        updatedHashedPassword = bcrypt.hashpw(req.POST['edit_password'].encode(), bcrypt.gensalt())
        userToUpdate.password = updatedHashedPassword

        userToUpdate.description = req.POST['edit_description']
        userToUpdate.save()

        return redirect('/dashboard/admin')

def edit_submit(req):
    errors = users.objects.update_user_validator(req.POST)

    if errors:
        for tag,error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/users/edit')

    else:
        userToUpdate = users.objects.get(id=req.POST['edit_id'])
        userToUpdate.first_name = req.POST['edit_first_name']
        userToUpdate.last_name = req.POST['edit_last_name']
        userToUpdate.email_address = req.POST['edit_email']
        req.session['email_address'] = req.POST['edit_email']
        updatedHashedPassword = bcrypt.hashpw(req.POST['edit_password'].encode(), bcrypt.gensalt())
        userToUpdate.password = updatedHashedPassword
        userToUpdate.description = req.POST['edit_description']
        userToUpdate.save()

        return redirect('/dashboard/admin')


def user_delete(req, user_id):
    userToDelete = users.objects.get(id=user_id)
    userToDelete.delete()
    return redirect('/dashboard')

def user_show(req, user_id):

    userToShow = users.objects.get(id=user_id)
    context = {
        'first_name': userToShow.first_name,
        'last_name': userToShow.last_name,
        'user_in_session' : req.session['email_address'],
        'created_at': userToShow.created_at,
        'user_id':userToShow.id,
        'email_address': userToShow.email_address,
        'description': userToShow.description,
        'messages': userToShow.messagespost.all().order_by('-created_at'),
        'comments': commentpost.objects.all()

    }

    return render(req, 'adminapp/show.html', context)

def message_post(req, user_id):
    receivingUser = users.objects.get(id=user_id)
    postingUser = users.objects.get(email_address=req.session['email_address'])
    messagePost = messagepost.objects.create(message=req.POST['form_message'],poster=postingUser,user_id=receivingUser)
    messagePost.save()
    return redirect('/users/show/{}'.format(user_id))

def comment_post(req, user_id, message_id):
    postingUser = users.objects.get(email_address=req.session['email_address'])
    messageComment = messagepost.objects.get(id=message_id)
    commentpost1 = commentpost.objects.create(comment=req.POST['form_comment'],user_id=postingUser,message_id=messageComment)
    commentpost1.save()
    return redirect('/users/show/{}'.format(user_id))
