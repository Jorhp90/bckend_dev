from movies.models import Movie
from django import forms

class UploadForm(forms.ModelForm):
    name = forms.CharField()
    image = forms.ImageField()

    class Meta:
        model = Movie
        fields = '__all__'
        #fields = ["name", "image"]
        #fields = ("name", "image")