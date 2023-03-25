from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """post table"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(null=True, blank=True, upload_to = 'Files')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
