from django.urls import path
from home.views import IndexView, get_data

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('api/', get_data, name='api'),
]
