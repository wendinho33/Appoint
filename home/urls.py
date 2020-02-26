from django.urls import path
from home.views import IndexView, get_data, UsersView, Todo_Delete, TodoUpdate


urlpatterns = [
    path('', IndexView, name='home'),
    path('delete/<int:pk>', Todo_Delete.as_view(), name='del'),
    path('edit/<int:pk>', TodoUpdate.as_view(), name='todo_update'),
    path('users/', UsersView.as_view(), name='users'),
    path('api/', get_data, name='api'),
]
