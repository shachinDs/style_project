from django.urls import path
from . import views

app_name="chat"
urlpatterns = [
    # this url is for each unique rooms
    path('<str:room>', views.room, name='room'),
    # this url for a view that will show all the messagaes to the room
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]