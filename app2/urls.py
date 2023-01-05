from django.urls import path
from app2.views import *
app_name='trip'

urlpatterns=[
    path('panda/',panda,name='panda'),
]