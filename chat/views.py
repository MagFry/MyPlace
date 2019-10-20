from django.shortcuts import render, redirect
from .models import Rooms
from . import forms
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required

@login_required
def room_list(request):
    room = Rooms.objects.all().order_by('date')
    return render(request, 'chat/room_list.html', {'rooms':room})

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

@login_required
def create_room(request):
    if request.method == 'POST':
        form = forms.CreateRoom(request.POST)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('chat:list')
    else:
        form = forms.CreateRoom()
    return render(request,'chat/room_create.html', {'form':form})

