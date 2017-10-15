from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.index),
    url(r'amadon/checkout', views.checkout),
    url(r'^amadon/buy/(?P<product_id>\d+)', views.process),
    url(r'^reset$', views.reset)
]
