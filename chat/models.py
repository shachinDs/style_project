from django.db import models
from datetime import datetime

# this is a room model, here all names of the room should be unique.
class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name



# this is message view, in this database we will store all the messages with some basic details.
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return self.room