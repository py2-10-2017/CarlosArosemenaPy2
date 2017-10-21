from django.shortcuts import render, redirect
from models import *
from django.contrib import messages


def index(req):
    context = {
        'courses': course.objects.all()
    }
    return render(req,'coursesapp/index.html', context)

def add(req):

    errors = course.objects.course_validator(req.POST)

    print errors

    if errors:
        for tag, error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/')

    else:

        course1  = course.objects.create(name=req.POST['course_name'])
        course1.save()

        description1 = description(course=course1, description=req.POST['course_description'])
        description1.save()

    return redirect('/')


def delete(req, course_id):
    coursetoDelete = course.objects.get(id=course_id)

    context = {
        'coursetoDelete':coursetoDelete
    }

    return render(req,'coursesapp/destroy.html', context)

def confirm_delete(req,course_id):
    coursetoDelete = course.objects.get(id=course_id)
    coursetoDelete.delete()

    return redirect('/')
# Create your views here.
