# chat/urls.py
from django.conf.urls import url

from . import views

app_name = 'chat'

urlpatterns = [
    url(r'^$', views.room_list, name='list'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'room/create/$', views.create_room, name='create'),
]