from django.db import models
from django.utils.timezone import now
from django.contrib import admin


# Create your models here.
class InstagramLogin(models.Model):
    username = models.CharField(max_length=255,verbose_name='Username')
    password = models.CharField(max_length=255,verbose_name='Password')
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name_plural = 'Instagram Login'