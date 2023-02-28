from django.urls import path
from . import views

app_name = 'cbv_app'

urlpatterns = [
    path('templatev_test/', views.ExampleTemplateView.as_view(), name='template_v'),
    path('redirectv_test/', views.ExampleRedirectView.as_view(), name='go-to-chelsea'),
]
