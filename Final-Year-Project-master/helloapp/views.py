from django.dispatch import receiver
from django.shortcuts import render, redirect
from .models import Profile, Location, Friend
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
import math
from django.urls import reverse
from chat.models import Room



# to find the distance brtween to coordinates, gives distance in killometer.
def distance(lat1, lon1, lat2, lon2):
    radius = 6371
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1) 
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d






# Create your views here.
def index_view(request):
    if not request.user.is_authenticated:
        return redirect('authentications:login')
    else:
        if request.method == 'POST':
            users = []

            longitude = request.POST["longitude"]
            latitude = request.POST["latitude"]
            if latitude and longitude:
                location = Location.objects.get(user=User.objects.get(username=request.user.username))
                location.latitude = latitude
                location.longitude = longitude
                location.save()

                others = Location.objects.exclude(user = User.objects.get(username=request.user.username))

                for other in others:
                    print ( f"{other.longitude} and {other.latitude} and {other.user.username}")
                    if (not other.user.username == "admin"):
                        lat1 = float(latitude)
                        lat2 = float(other.latitude)
                        lon1 = float(longitude)
                        lon2 = float(other.longitude)

                        p = distance(lat1, lon1, lat2, lon2)
                        print (f"the current distance is : {p} kilometers")
                        # give me all the people who are in the distance of 100 meters
                        if p < 0.3:
                            users.append(other.user.username)
                            print (f"all the people near you are : {users}")

                return render(request, "helloapp/index.html",
                    {   
                    "peoples" : users,
                    }
                )
            else:
                return HttpResponseRedirect(reverse("authentications:login"))
        else:
            request_list = []
            friend_requests = Friend.objects.filter(receiver=request.user.username)
            for requests in friend_requests:
                request_list.append(str(requests))
            
            return render(request, "helloapp/index.html", {"friend_request" : request_list})










def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('authentications:login')
    
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=User.objects.get(username=request.user.username))

        if not request.user.first_name == request.POST['first_name']:
            user.first_name = request.POST['first_name']

        if not request.user.last_name == request.POST['last_name']:
            user.last_name = request.POST['last_name']

        if not request.user.username == request.POST['username']:
            if not User.objects.filter(username = request.POST['username']).exists():
                user.username = request.POST['username']
            else:
                return render(request, "helloapp/profile.html", {"message" : f"{request.POST['username']} is already taken!"})

        if not request.user.email == request.POST['email']:
            if not User.objects.filter(email=request.POST['email']).exists():
                user.email = request.POST['email']
            else:
                return render(request, "helloapp/profile.html", {"message" : f"{request.POST['email']} is already taken!"})

        if not profile.bio == request.POST['bio']:
            profile.bio = request.POST['bio']

        if not profile.gender == request.POST['gender']:
            profile.gender = request.POST['gender']

        if not profile.relationship == request.POST['relationship']:
            profile.relationship = request.POST['relationship']
        
        if request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        user.save()
        profile.save()
        return redirect('helloapp:index')
    else:
        return render(request, "helloapp/profile.html")







def user_details_view(request, username):
    if not request.user.is_authenticated:
        return redirect('authentications:login')

    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)


    if request.method == 'POST':
        sender = request.POST['sender']
        receiver = request.POST['receiver']
        
        if not Friend.objects.filter(sender=sender, receiver=receiver).exists():

            p1 = Location.objects.get(user = User.objects.get(username=sender))
            p2 = Location.objects.get(user = User.objects.get(username=receiver))
            lat1 = p1.latitude
            lat2 = p2.latitude
            lon1 = p1.longitude
            lon2 = p2.longitude

            d = distance(lat1, lon1, lat2, lon2)
            
            if d < 0.3:
                friend = Friend()
                friend.sender = sender
                friend.receiver = receiver
                friend.save()
        
        room_name = str(sender+receiver)
        
        if not Room.objects.filter(name=room_name).exists():
            room = Room()
            room.name = room_name
            room.save()
        


    return render(request, "helloapp/user_details.html", 
        {
            "profile_picture" : profile.profile_picture,
            "profile_bio" : profile.bio,
            "profile_gender" : profile.gender,
            "profile_relationship" : profile.relationship,
            "user_first_name" : user.first_name,
            "user_last_name" : user.last_name,
            "username" : user.username,
        }
    )