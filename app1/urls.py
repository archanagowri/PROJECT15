from django.urls import path
from app1.views import *
app_name='pip'

urlpatterns=[
    path('pranitha/',pranitha,name='pranitha'),
]