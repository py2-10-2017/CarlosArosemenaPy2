from django.shortcuts import render, HttpResponse,redirect
from models import users
from django.contrib import messages

# Create your views here.
def index(req):
    allusers = users.objects.all()
    lastuser = users.objects.last()
    firstuser = users.objects.first()
    allusersDESC = users.objects.order_by("-first_name")

    context = {
        'allusers': allusers,
        'lastuser': lastuser,
        'firstuser': firstuser,
        'allusersDESC':allusersDESC

    }

    print context

    return render(req,'userapp/index.html',context )


def create(req):
    errors = users.objects.user_validator(req.POST)

    if errors:
            for tag, error in errors.iteritems():
                messages.error(req,error,extra_tags=tag)
                return redirect('/')
    else:
        newuser = users.objects.create(first_name=req.POST['first_name'],last_name=req.POST['last_name'],email_address=req.POST['email_address'],age=req.POST['age'])
    # req.session[newuser]=newuser

    return redirect('/')

def update(req):
    usertoUpdate = users.objects.get(id=req.POST['updateid'])
    usertoUpdate.last_name = req.POST['updateLastname']
    usertoUpdate.save()

    return redirect('/')

def delete(req):
    usertoDelete = users.objects.get(id=req.POST['deleteid'])
    usertoDelete.delete()

    return redirect('/')
