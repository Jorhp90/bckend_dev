from django.urls import path
from . import views

app_name = 'the_polls'

urlpatterns = [
    path("", views.index, name='index_v'),
    path("<int:question_id_i>/", views.detail, name='detail_v'),
    path("<int:question_id_i>/vote/", views.vote, name='vote_v'),
    path("<int:question_id_i>/<int:choice_id_i>/results/", views.results, name='results_v'),
    path("summary/", views.summary, name="summary_v"),
]
