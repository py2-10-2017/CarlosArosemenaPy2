from __future__ import unicode_literals
from ..log_reg.models import *

from django.db import models

class DataManager(models.Manager):
    def validate_review(self, postData):
        errors = {}

        if len(postData['book_title'])<1 and len(postData['review'])<1:
            errors['data']='All fields are required'

        if Book.objects.filter(title=postData['book_title']):
            errors['book']='Book already exists, please see list to add review'

        if postData['existing_author'] == 'none' and len(postData['new_author'])<3:
            errors['author']='Please select an author or include a valid new one'

        if not postData['rating']:
            errors['rating']='Please select a rating'

        return errors

    def create_review(self,postData,user_id):
        #let's create the author

        if postData['existing_author'] and len(postData['new_author']) == 0:
            author = Author.objects.create(author_name=postData['existing_author'])
        elif postData['new_author']:
            author = Author.objects.create(author_name=postData['new_author'])

        #let's create the book

        book = Book.objects.create(title=postData['book_title'],author=author)

        review = Review.objects.create(review=postData['review'],
                                       rating=postData['rating'],
                                       book=book,
                                       reviewer=users.objects.get(id=user_id) )

        return review
    
    def recent_and_old(self):
        return(self.all().order_by('-created_at')[:3],self.all().order_by('created_at')[3:])



class Author(models.Model):
    author_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews')
    reviewer = models.ForeignKey(users, related_name='reviews_left')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DataManager()
