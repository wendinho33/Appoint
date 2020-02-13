from django.urls import path
from meeting.views import AppointList, AppointCreate, AppointUpdate, AppointDetail, AppointSearch

urlpatterns = [
    path('search/', AppointSearch.as_view(), name='search_meeting'),
    path('', AppointList.as_view(), name='meeting-list'),
    path('create/', AppointCreate.as_view(), name='meeting-create'),
    path('<slug:slug>/edit/', AppointUpdate.as_view(), name='meeting-update'),
    path('<slug:slug>/', AppointDetail.as_view(), name='meeting-detail'),


]
