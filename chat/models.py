from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Rooms(models.Model):
    name_of_room = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    date = models.DateField(auto_now_add = True)
    author = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_room

    def short_description(self):
        return self.description[:30]+"..."