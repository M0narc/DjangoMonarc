from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
import datetime


# Create your views here.
def index(request):
    return HttpResponse("<html><body><h1>dale anda la puta madre jajaja</h1></body></html>")


def to_do_list(request, id):
    """
    here we GET the object by id in our ToDoList tab from
    our db and display it's name using ls.name,
    even though objects.get is not part of python, it will work
    the same will happen with ls.name
    """
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, item.text))


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

