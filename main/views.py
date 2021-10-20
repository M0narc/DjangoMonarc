from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def index(request):
    return HttpResponse("<html><body><h1>dale anda la puta madre jajaja</h1></body></html>")


def v1(request):
    return HttpResponse("view 1")


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

