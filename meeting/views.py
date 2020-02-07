from django.shortcuts import render
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from meeting.forms import AppointmentForm
from django.urls import reverse_lazy
from meeting.models import Appointment


# Create your views here.

class AppointCreate(BSModalCreateView, LoginRequiredMixin):
    login_url = 'login'
    form_class = AppointmentForm
    template_name = 'meeting/create.html'
    success_message = 'Appointment has been created successfully'
    success_url = reverse_lazy('meeting-list')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)


class AppointUpdate(BSModalUpdateView, LoginRequiredMixin):
    login_url = 'login'
    form_class = AppointmentForm
    queryset = Appointment.objects.all()
    template_name = 'meeting/edit.html'
    success_message = 'Appointment Updated Successfully'
    success_url = reverse_lazy('meeting-list')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)


class AppointList(ListView, LoginRequiredMixin):
    login_url = 'login'
    model = Appointment
    queryset = Appointment.objects.order_by('-published')
    context_object_name = 'meetings'
    template_name = 'meeting/index.html'
    paginate_by = 10


class AppointDetail(BSModalReadView, LoginRequiredMixin):
    login_url = 'login'
    model = Appointment
    template_name = 'meeting/detail.html'
    queryset = Appointment.objects.all()
    context_object_name = 'appoint'
