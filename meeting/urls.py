from django.urls import path
from meeting.views import AppointList, AppointCreate, AppointUpdate

urlpatterns = [
    path('', AppointList.as_view(), name='meeting-list'),
    path('create/', AppointCreate.as_view(), name='meeting-create'),
    path('<slug:slug>/edit/', AppointUpdate.as_view(), name='meeting-update'),

]