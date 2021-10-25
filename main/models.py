from django.db import models


# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    # when we delete an item in TDL this item should be deleted as well
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    # this represents whether or not we completed an item in our TDL
    complete = models.BooleanField()

    def __str__(self):
        return self.text

