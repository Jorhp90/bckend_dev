from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
#django will join all directories called templates, then look on core

def contact(request):
    return render(request, 'core/contact.html')