from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User

def index(request):
    return render(request, "work_analizer/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("work_analizer:index"))
        else:
            return render(request, "work_analizer/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "work_analizer/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("work_analizer:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "work_analizer/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "work_analizer/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("work_analizer:index"))
    else:
        return render(request, "work_analizer/register.html")

