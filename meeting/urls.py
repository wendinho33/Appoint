from django.urls import path
from meeting.views import AppointList, AppointCreate

urlpatterns = [
    path('', AppointList.as_view(), name='meeting-list'),
    path('create/', AppointCreate.as_view(), name='meeting-create'),

]