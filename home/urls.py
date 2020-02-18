from django.urls import path
from home.views import IndexView, get_data, UsersView, remove


urlpatterns = [
    path('', IndexView, name='home'),
    path('delete/<int:todo_id>', remove, name='del'),
    path('users/', UsersView.as_view(), name='users'),
    path('api/', get_data, name='api'),
]
