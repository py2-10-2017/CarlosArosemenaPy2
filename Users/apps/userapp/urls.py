from . import views
from django.conf.urls import url

urlpatterns= [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^update$', views.update),
    url(r'^delete$', views.delete)
]
