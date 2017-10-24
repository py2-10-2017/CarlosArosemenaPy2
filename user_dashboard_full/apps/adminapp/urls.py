from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^dashboard/admin$',views.dashboard, name="dashboardadmin"),
    url(r'^dashboard$',views.dashboard, name="dashboard"),
    url(r'^users/new', views.render_regform)

]
