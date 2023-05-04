from django.contrib import admin
from dwitter.models import CustomUser, Profile, Dweet

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    fields = ['email', 'username']
    inlines = [ProfileInline]

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Dweet)