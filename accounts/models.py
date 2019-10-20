from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default='9999-12-31')
    faculty = models.CharField(default=' ', max_length=20)
    city = models.CharField(default=' ', max_length=20)
    phone = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return str(self.user)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])




