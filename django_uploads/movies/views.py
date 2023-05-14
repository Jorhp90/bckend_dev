from django.shortcuts import render, redirect
from movies.forms import UploadForm
from movies.models import Movie

def upload1(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES.get('image_upload')

        new_movie = Movie.objects.create(name = name, image=image)
        new_movie.save()
        return redirect('home_view')
    else: 
        return redirect('/')
        
        
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_view')
        else:
            return redirect('wrong_view')
    
    context = {'form': UploadForm}
    return render(request, template_name='movies/upload.html', context=context)

def home(request):
    return render(request, template_name='movies/home.html')

def wrong(request):
    return render(request, template_name='movies/wrong.html')