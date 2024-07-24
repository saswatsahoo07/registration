from django.urls import path
from .views import *
urlpatterns = [
    path('Register', register, name='register')
]