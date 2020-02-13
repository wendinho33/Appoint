from django.urls import path
from meeting.views import AppointList, AppointCreate, AppointUpdate, AppointDetail, AppointSearch, AddressCreate, AddressList, AddressUpdate

urlpatterns = [
    path('search/', AppointSearch.as_view(), name='search_meeting'),
    path('', AppointList.as_view(), name='meeting-list'),
    path('create/', AppointCreate.as_view(), name='meeting-create'),
    path('create/address/', AddressCreate.as_view(), name='address-create'),
    path('address/', AddressList.as_view(), name='address-list'),
    path('address/<int:pk>', AddressUpdate.as_view(), name='address-update'),
    path('<slug:slug>/edit/', AppointUpdate.as_view(), name='meeting-update'),
    path('<slug:slug>/', AppointDetail.as_view(), name='meeting-detail'),


]
