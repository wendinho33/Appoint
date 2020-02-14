from django.urls import path
from home.views import IndexView, get_data, UsersView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('users/', UsersView.as_view(), name='users'),
    path('api/', get_data, name='api'),
]
