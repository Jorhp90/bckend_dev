from django.urls import path
from movies.views import upload, home, wrong

urlpatterns = [
    path("home", home, name="home_view"),
    path("wrong", wrong, name="wrong_view"),
    path("movies/upload", upload, name="upload_view"),
]