from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^dashboard/admin$',views.dashboardadmin, name="dashboardadmin"),
    url(r'^dashboard$',views.dashboard, name="dashboard"),
    url(r'^users/new$', views.render_regform),
    url(r'^users/submit$', views.submit_new_user),
    url(r'^users/edit$', views.render_edit),
    url(r'^edit/submit$', views.edit_submit),
    url(r'^edit/submit/(?P<user_id>\d+)$', views.edit_single_submit),
    url(r'^users/edit/(?P<user_id>\d+)$', views.render_single_edit),
    url(r'^users/delete/(?P<user_id>\d+)$', views.user_delete),
    url(r'^users/show/(?P<user_id>\d+)$', views.user_show),
    url(r'^users/message/(?P<user_id>\d+)$', views.message_post),
    url(r'^users/comment/(?P<message_id>\d+)/(?P<user_id>\d+)$', views.comment_post),


]
