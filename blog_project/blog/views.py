from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Inicia el Blog")

class HomeView(TemplateView):
    template_name = 'blog/index.html'