from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created!")
            return redirect('index_view')
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)
