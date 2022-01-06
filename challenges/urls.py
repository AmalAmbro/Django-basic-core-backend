from django.urls import path

from . import views

urlpatterns=[
    path("", views.index), #challenges/ 
    path("<int:month>", views.challenge_for_no),
    path("<str:month>", views.challenge_function, name="month-challenge")
]