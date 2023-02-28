from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls_i/', include('polls.urls')),
    path('cbv/', include('cbv.urls')),
]
