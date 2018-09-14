from django.conf.urls import url
from home.views import *

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home')

]
