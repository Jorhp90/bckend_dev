from django.urls import path
from . import views
#from .views import IndexView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'the_polls'

urlpatterns = [
    #path("", views.index, name='index_v'),
    path("", views.IndexView.as_view(), name='index_v'),

    path("<int:question_id_i>/", views.detail, name='detail_v'),
    #path("<int:pk>/", views.DetailView.as_view(), name='detail_v'),
    
    path("<int:question_id_i>/vote/", views.vote, name='vote_v'),
    path("<int:question_id_i>/<int:choice_id_i>/results/", views.results, name='results_v'),
    path("summary/", views.summary, name="summary_v"),
    path("register/", views.register_form, name='register_v'),

    path("login/", LoginView.as_view(template_name='polls/login.html'), name='login_v'),
    path("logout/", LogoutView.as_view(), name='logout_v'),
]
