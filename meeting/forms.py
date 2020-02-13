from bootstrap_modal_forms.forms import BSModalForm
from meeting.models import Appointment, Place_Of_Residence
from django import forms


class AppointmentForm(BSModalForm):
    class Meta:
        model = Appointment
        exclude = ['staff', 'slug', 'published', 'created_at', 'updated_at']


class AddressForm(BSModalForm):
    class Meta:
        model = Place_Of_Residence
        fields = '__all__'
