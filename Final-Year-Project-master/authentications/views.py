import profile
from django.shortcuts import render, redirect
from .forms import ModifiedUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from helloapp.models import Profile, Location
from django.contrib.auth.models import User


# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        form = ModifiedUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            profile = Profile()
            location = Location()
            profile.user = User.objects.get(username=username)
            location.user = User.objects.get(username=username)
            location.save()
            profile.save()
            messages.success(request, f"{username} is successfully registered!")
            return redirect('authentications:login')
        else:
            username = form.cleaned_data.get('username')
            messages.error(request, f"somthing worng with {username} user!")
            return render(request, "authentications/registration.html", 
                {"form" : form}
            )
    else:
        form = ModifiedUserCreationForm()
        return render(request, "authentications/registration.html", 
            {"form" : form}
        )





def login_view(request):
    if request.user.is_authenticated:
        return redirect("helloapp:index")
    else:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username} is successfully logged in")
                return redirect('helloapp:index')
            else:
                messages.error(request, f"{username} is not varified!")
                return render(request, "authentications/login.html")
        else:
            return render(request, "authentications/login.html")





def logout_view(request):
    username = request.user.username
    logout(request) 
    messages.success(request, f"{username} is successfully logged out!")
    return redirect('authentications:login')