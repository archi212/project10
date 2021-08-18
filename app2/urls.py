from django.conf.urls import url
from django.urls import path
from django.urls import path
from app2.views import *
app_name='app2'

urlpatterns=[
    path('app2_bye/',app2_bye,name='app2_bye'),
]