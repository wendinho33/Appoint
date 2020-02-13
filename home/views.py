from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from meeting.models import Appointment
from django.contrib.auth.decorators import login_required


# Create your views here.

class IndexView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Appointment
    template_name = 'home/index.html'
    queryset = Appointment.objects.all()
    context_object_name = 'appointment'


@login_required(login_url='login')
def get_data(request, *args, **kwargs):
    if request.user.is_superuser:
        qs = Appointment.objects.all().count()
        data = {'meetings': qs}
        return JsonResponse(data, safe=False)
