from django.urls import path
from app.views import *

urlpatterns = [
    path('hello/', hello_res, name='hello')
]
