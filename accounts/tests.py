from django.test import TestCase
from django.contrib.auth.models import User


class UserProfileModelTest1(TestCase):

    def test_string_representation(self):
        user_prof = User(username = "Aga")
        self.assertEqual(str(user_prof), user_prof.username)

class UserProfileModelTest2(TestCase):

    def test_string_representation(self):
        user_prof = User(username = "Mag")
        self.assertEqual(str(user_prof), user_prof.username)

class UserProfileModelTest3(TestCase):

    def test_string_representation(self):
        user_prof = User(username = "Janek")
        self.assertEqual(str(user_prof), user_prof.username)

class MyPlaceTests1(TestCase):

    def test_page(self):
        response = self.client.get('/accounts')
        self.assertEqual(response.status_code, 404)

class MyPlaceTests2(TestCase):

    def test_page(self):
        response = self.client.get('/account')
        self.assertEqual(response.status_code, 301)

class MyPlaceTests3(TestCase):

    def test_page(self):
        response = self.client.get('/account/profile')
        self.assertEqual(response.status_code, 301)

class MyPlaceTests4(TestCase):

    def test_page(self):
        response = self.client.get('/account/edit')
        self.assertEqual(response.status_code, 301)

class MyPlaceTests5(TestCase):

    def test_page(self):
        response = self.client.get('/account/signup')
        self.assertEqual(response.status_code, 301)