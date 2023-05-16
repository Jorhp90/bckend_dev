from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm

def register(request):
    if request.method == 'GET':
        context = {'form':CustomUserCreationForm}
        return render(request, "users/register.html", context=context)
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home_view'))