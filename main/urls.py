from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("fecha/", views.show_date, name="Fecha actual"),
    path("todo/<int:id>", views.to_do_list, name="ToDoList")
]
