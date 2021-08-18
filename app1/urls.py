from django.urls import path
from django.urls import path
from app1.views import *
app_name='app1'

urlpatterns=[
    path('app1_hai/',app1_hai,name='app1_hai'),

]