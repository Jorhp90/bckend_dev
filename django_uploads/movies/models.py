from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return self.name
