from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True)
    theme = models.CharField(max_length=10, default='light')
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        default=settings.DEFAULT_PROFILE_IMAGE
    )
    def __str__(self):
        return self.username
    
    def toggle_theme(self):
        self.theme = 'dark' if self.theme == 'light' else 'light'
        self.save()

class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)