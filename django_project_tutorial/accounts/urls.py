from django.conf.urls import url
from . import views #looks for views in main level
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name':'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^change-password$', views.change_password, name='change_password')
]
