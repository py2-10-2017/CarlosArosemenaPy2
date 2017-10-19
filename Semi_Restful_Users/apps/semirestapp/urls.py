from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<user_id>\d+)/update$', views.update),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.delete)


]

##Generated a TypeError at /admin/ argument to reversed() must be a sequence cuz I had urlpatterns = {} instead
##of urlpatterns = []
