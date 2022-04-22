from django.urls import path
from . import views

urlpatterns = [

    path('actors/',views.actor_list)
]