from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    datacompleted = models.DateField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle + '- by ' + self.user.username