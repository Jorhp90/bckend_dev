from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name='login_v'),
    path("logout/", LogoutView.as_view(next_page='tasks_v'), name = 'logout_v'), 
    path("register/", RegisterPage.as_view(), name='register_v'),

    path("", TaskList.as_view(), name='tasks_v'),
    path("task_j/<int:pk>", TaskDetail.as_view(), name='detail_v'),
    path("task-create/", TaskCreate.as_view(), name='task_create_v'),
    path("task-update/<int:pk>", TaskUpdate.as_view(), name='task_update_v'),
    path("task-delete/<int:pk>", TaskDelete.as_view(), name='task_delete_v'),
]

