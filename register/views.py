from django.shortcuts import render, redirect
# since we do not want duplicate code we just import RegisterForm from forms.py
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        # once it's created it redirects to our home
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
