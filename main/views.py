from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
import datetime


# Create your views here.
def index(response):
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})


def to_do_list(response, id):
    """
    here we GET the object by id in our ToDoList tab from
    our db and display it's name using ls.name,
    even though objects.get is not part of python, it will work
    the same will happen with ls.name
    """
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})


def show_date(request):
    current_date = datetime.datetime.now()

    document = """<html>
    <body>
    <h1>
    fecha y hora actual es %s 
    </h1>
    </body>
    </html>""" % current_date
    return HttpResponse(document)

