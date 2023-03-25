from django.urls import path
from blog import views

urlpatterns = [
    #path("", views.index, name="index_view"),
    path("", views.HomeView.as_view(), name='home_view'),
]
