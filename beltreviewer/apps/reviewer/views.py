from django.shortcuts import render, redirect, HttpResponse
from models import *
from ..log_reg.models import *
from django.contrib import messages


def index(req):
    context = {
        'user_in_session': req.session['first_name'],
        'recent':Review.objects.recent_and_old()[0],
        'old': Book.objects.all()
    }
    return render(req,'reviewer/index.html', context)

def book_form(req):
    context = {
        'user_id': req.session['user_id'],
        'user_in_session': req.session['first_name'],
        'authors': Author.objects.all()
    }
    return render(req, 'reviewer/bookadd.html', context)

def book_post(req,user_id):
    errors = Review.objects.validate_review(req.POST)

    if errors:
        for tag,error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/books/add')

    book_review = Review.objects.create_review(req.POST, user_id)


    return redirect('/books/{}'.format(book_review.book.id))

def book_show(req,book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book':book,
        'reviews':book.reviews.all(),
        'user_id': req.session['user_id'],
        'user_in_session': req.session['first_name']
    }
    return render(req,'reviewer/book.html', context)

def user_show(req, user_id):
    user = users.objects.get(id=user_id)
    context = {
        'user': user.email_address,
        'user_in_session': req.session['first_name'],
        'first_name': user.first_name,
        'last_name': user.last_name,
        'reviews': user.reviews_left.count(),
        'books': user.reviews_left.all()

    }
    return render(req, 'reviewer/userinfo.html', context)


def user_add_review(req, book_id):

    book = Book.objects.get(id=book_id)

    user_id = users.objects.get(id=req.session['user_id'])

    Review.objects.create(review=req.POST['review'],
                                   rating=req.POST['rating'],
                                   book=book,
                                   reviewer=user_id)

    return redirect('/books/{}'.format(book_id))

def delete_review(req, review_id, book_id):
    review_delete = Review.objects.get(id=review_id)
    review_delete.delete()
    

    return redirect('/books/{}'.format(book_id))


# Create your views here.
