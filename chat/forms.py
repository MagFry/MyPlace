from django import forms
from . import models


class CreateRoom(forms.ModelForm):
    class Meta:
        model = models.Rooms
        fields = ['name_of_room', 'description']
