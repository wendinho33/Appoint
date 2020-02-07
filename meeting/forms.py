from bootstrap_modal_forms.forms import BSModalForm
from meeting.models import Appointment


class AppointmentForm(BSModalForm):
    class Meta:
        model = Appointment
        exclude = ['staff', 'slug', 'published', 'created_at', 'updated_at']
