from django.urls import path
from dwitter.views import dashboard, profile_list, profile

app_name = "dwitter_app"

urlpatterns = [
    path("", dashboard, name="dashboard_view"),
    path("profile_list/", profile_list, name="profile_list_view"),
    path("profile/<int:pk>/", profile, name="profile_view"), #Django’s angled-bracket syntax,allows 2 capture path components
]
