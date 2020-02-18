from django.urls import path
from account.views import user_login, user_logout, validate_username

urlpatterns = [
    path('', user_login, name='login'),
    path('validate/', validate_username, name='validate'),
    path('logout/', user_logout, name='logout'),
]
