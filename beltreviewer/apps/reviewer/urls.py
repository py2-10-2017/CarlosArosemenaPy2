from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.index, name='books'),
    url(r'^books/add$', views.book_form),
    url(r'^books/post/(?P<user_id>\d+)$', views.book_post),
    url(r'^books/(?P<book_id>\d+)$', views.book_show),
    url(r'^users/(?P<user_id>\d+)$', views.user_show),
    url(r'^books/reviewpost/(?P<book_id>\d+)$', views.user_add_review),
    url(r'^delete/(?P<review_id>\d+)/(?P<book_id>\d+)$', views.delete_review)
]
