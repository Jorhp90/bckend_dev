from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """post table"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(null=True, blank=True, upload_to = 'Files')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now, auto_now=True)

    def __str__(self):
        return self.title
    
class Test(models.Model):
    title = models.CharField(max_length=200)
    
class TestTable2(models.Model):
    content = models.CharField(max_length=100)