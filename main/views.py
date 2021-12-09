from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
import datetime


# Create your views here.
def index(response):
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        # this is holding all the info of our form in a dictionary
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})


def to_do_list(response, id):
    """
    here we GET the object by id in our ToDoList tab from
    our db and display it's name using ls.name,
    even though objects.get is not part of python, it will work
    the same will happen with ls.name
    we also interact with the list.html in order to update the
    checkboxes and add new items in our lists
    :param id: ToDoList id
    """
    # first we instantiate the todolist objects id
    ls = ToDoList.objects.get(id=id)
    # if the response method from the list.html is POST run the code below
    if response.method == "POST":
        print(response.POST)
        # the name of the BUTTON in list.html
        if response.POST.get("save"):
            for item in ls.item_set.all():
                # the checkbox id's have a "c" before the id, if it's cicked this is true otherwise it isn't :v
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                # remember to save!
                item.save()

        # here we're clicking new item button, besides the textbox
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                # item_set is kinda like a setter from any other object
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid")
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
