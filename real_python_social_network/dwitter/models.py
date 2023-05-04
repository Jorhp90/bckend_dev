from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
#from PIL import pillow

class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    username = models.CharField(max_length=20)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

class Profile(models.Model):
    email = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.email.username
    
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         user_profile = Profile(user=instance) #user being the Foreign Key that connects Profile with main User model
#         user_profile.save()
# # Create a Profile for each new user.
# post_save.connect(create_profile, sender=User)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(email=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

class Dweet(models.Model):
    email = models.ForeignKey(
        CustomUser,
        related_name="dweets", #allows access dweet objects from the user side through .dweets
        on_delete=models.DO_NOTHING, #orphaned dweets should stick around
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("""
        {}
        :({:%Y-%m-%d %H:%M})
        {}
        """.format(self.email, self.created_at, self.body[:30]))

