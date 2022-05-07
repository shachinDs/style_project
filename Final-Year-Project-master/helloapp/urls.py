from django.urls import path
from . import views

app_name = 'helloapp'
urlpatterns = [
    path('', views.index_view, name="index"),
    path('profile', views.profile_view, name="profile"),
    path('<str:username>', views.user_details_view, name="user_details"),
]