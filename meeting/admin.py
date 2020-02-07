from django.contrib import admin
from meeting.models import Appointment, Place_Of_Residence


# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['first_Name', 'last_Name', 'NIC', 'created_at']

@admin.register(Place_Of_Residence)
class Place_Of_Residence(admin.ModelAdmin):
    list_display = ['address', 'region']