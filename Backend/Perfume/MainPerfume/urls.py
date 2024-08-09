from django.urls import path
from .views import *

urlpatterns = [
   path("Home/<int:pk>",UserManagerWith.as_view()),
   path("Home/",UserManagerWithout.as_view()),
]
