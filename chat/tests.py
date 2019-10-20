from django.test import TestCase
from .models import Rooms
# Create your tests here.

class RoomsModelTest1(TestCase):

    def test_string_representation(self):
        room = Rooms(name_of_room = "Cinema")
        self.assertEqual(str(room), room.name_of_room)

class RoomsModelTest2(TestCase):

    def test_string_representation(self):
        room = Rooms(name_of_room = "City")
        self.assertEqual(str(room), room.name_of_room)

class RoomsModelTest3(TestCase):

    def test_string_representation(self):
        room = Rooms(name_of_room = "Books")
        self.assertEqual(str(room), room.name_of_room)

class MyPlaceTests1(TestCase):

    def test_page(self):
        response = self.client.get('/chat')
        self.assertEqual(response.status_code, 301)

class MyPlaceTests2(TestCase):

    def test_page(self):
        response = self.client.get('/chat/room/create')
        self.assertEqual(response.status_code, 301)