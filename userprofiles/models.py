from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class UserProfile(models.Model):
    avatar = ImageField(upload_to='avatars', null=True, blank=True)
    user = models.OneToOneField(User)

    @classmethod
    def create_user_with_profile(cls, user):
        us = User.objects.create_user(username=user['username'], first_name=user['name'],
                                      last_name=user['last_name'], password=user['password'],
                                      email=user['email'])
        user_profile = cls(avatar=user['avatar'], user=us)
        user_profile.save()

    def __str__(self):
        return self.user.username
