from bootstrap_modal_forms.forms import BSModalForm
from meeting.models import Appointment
from django import forms


class AppointmentForm(BSModalForm):
    class Meta:
        model = Appointment
        exclude = ['staff', 'slug', 'published', 'created_at', 'updated_at']


class SearchForm(forms.Form):
    query = forms.CharField()
