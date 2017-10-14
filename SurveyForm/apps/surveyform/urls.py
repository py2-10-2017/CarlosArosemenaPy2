from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process$', views.process),
    url(r'^result$', views.result)
]
