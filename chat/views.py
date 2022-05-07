from django.shortcuts import redirect, render
from .models import Message
from django.http import HttpResponse, JsonResponse


# Create your views here.

# this is a unique room for two people to chat. this room is unique cause it made by two people's username
def room (request, room):
    # checking the user is authenticated or not
    if not request.user.is_authenticated:
        return redirect('authentications:login')
    
    # if somebody wants to post any message then save the message into the database. Each message can be identify by using their room name
    if request.method == 'POST':
        message = Message()
        message.value = request.POST['message']
        message.user = request.POST['username']
        message.room = request.POST['room_id']
        message.save()

    # normally just render the simple template with a parameter room name.
    return render(request, "chat/room.html", {'room' : room})



# this view is for showing the messagaes that have been sent to the room
def getMessages(request, room):
    # checking is the user authenticated or not
    if not request.user.is_authenticated:
        return redirect('authentications:login')

    # get all the messagaes that have been sent to the specific room
    messages = Message.objects.filter(room=room)
    # get all the messages and send it back to the room templete to show the chats.
    return JsonResponse({"messages":list(messages.values())})