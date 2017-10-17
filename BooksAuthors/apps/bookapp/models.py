from django.db import models
#Create a new model called 'Book' with the information above.
#Create a new model called 'Author' with the information above.  Design the models in a way that you could perform the

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
