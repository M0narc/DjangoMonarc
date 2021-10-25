from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("fecha/", views.show_date, name="Fecha actual"),
    path("todo/<int:id>", views.to_do_list, name="ToDoList")
]
