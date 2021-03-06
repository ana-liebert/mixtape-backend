from django.db import models
import time
from django.conf import settings
from django.contrib.postgres.fields import ArrayField



class Genre(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

SCHEDULE_CHOICES = (
    ("monthly", "Monthly"),
    ("weekly", "Weekly"),
    ("guest", "Guest Spot"),
)

class Host(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 800)
    image = models.CharField(max_length = 200)
    schedule = models.CharField(max_length=50, choices=SCHEDULE_CHOICES)

    def __str__(self):
        return self.name

class Mix(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name="hosts")
    image = models.CharField(max_length = 200)
    genre = models.ManyToManyField(Genre, blank=True)
    soundcloudplayer = models.CharField(max_length = 500)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mixpost")
    
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    favorites = models.ManyToManyField(Mix, related_name='mixes')