from  .views import *
from django.urls import path

urlpatterns=[
    path('app2/',home2,name='app2')
]