from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "chat/index.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("USER CREATED:", user)
            return redirect("/accounts/login/")
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = UserCreationForm()

    return render(request, "chat/signup.html", {"form": form})

@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
