from django.db import models
from config.models import TimeStampMixin
from django.contrib.auth.models import User

# Create your models here.

class Task(TimeStampMixin,models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tasks')
    
    
    def __str__(self):
        return self.title
        