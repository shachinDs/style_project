from django.contrib import admin
from .models import Profile,Location,Friend

# Register your models here.
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Friend)