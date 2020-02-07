from django.urls import path
from meeting.views import AppointList

urlpatterns = [
    path('', AppointList.as_view(), name='meeting-list'),

]