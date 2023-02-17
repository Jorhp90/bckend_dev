from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__' #all fields from LoginView form
    redirect_authenticated_user = True #prevent from an authenticated user gets in the login page

    #success_url = reverse_lazy('tasks_v')
    def get_success_url(self):
        return reverse_lazy('tasks_v')

# Create your views here.
class TaskList(ListView):
    """template with query-set updated"""
    model = Task
    context_object_name = 'tasks' #change the context object name for the template

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html' #add the specific template to connect

class TaskCreate(CreateView):
    model = Task
    fields = '__all__' #all the fields from the model
    success_url = reverse_lazy('tasks_v')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__' #all the fields from the model
    success_url = reverse_lazy('tasks_v')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_v')