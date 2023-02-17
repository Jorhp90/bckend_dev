from django.db import models
from django.contrib.auth.models import User #native user model

# Create your models here.
class Task(models.Model):
    #one to many relationship, one user many tasks
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #models.SET_NULL if you delete the user remains the task
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] #sort by completion