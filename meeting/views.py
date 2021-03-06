from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import JsonResponse
from meeting.forms import AppointmentForm, AddressForm
from meeting.models import Appointment, Place_Of_Residence


# Create your views here.
class AddressCreate(LoginRequiredMixin, BSModalCreateView):
    login_url = 'login'
    form_class = AddressForm
    template_name = 'meeting/address.html'
    success_message = 'Address successfully Created'
    success_url = reverse_lazy('meeting-list')


def validate_address(request):
    address = request.GET.get('address', None)
    data = {
        'is_taken': Place_Of_Residence.objects.filter(address__iexact=address).exists()
    }
    return JsonResponse(data)


class AddressUpdate(LoginRequiredMixin, BSModalUpdateView):
    login_url = 'login'
    form_class = AddressForm
    template_name = 'meeting/address_update.html'
    queryset = Place_Of_Residence.objects.all()
    success_message = 'Address successfully Added'
    success_url = reverse_lazy('address-list')


class AddressList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Place_Of_Residence
    queryset = Place_Of_Residence.objects.all().order_by('address')
    template_name = 'meeting/address_list.html'
    context_object_name = 'addresses'


class AppointCreate(LoginRequiredMixin, BSModalCreateView):
    login_url = 'login'
    form_class = AppointmentForm
    template_name = 'meeting/create.html'
    success_message = 'Appointment has been created successfully'
    success_url = reverse_lazy('meeting-list')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)


def validate_name(request):
    first = request.GET.get('first_Name', None)
    last = request.GET.get('last_Name', None)
    tel = request.GET.get('telephone', None)
    data = {
        'exists': Appointment.objects.filter(first_Name__iexact=first).exists(),
        'exists2': Appointment.objects.filter(last_Name__iexact=last).exists(),
        'exists3': Appointment.objects.filter(telephone__exact=tel).exists(),
    }
    return JsonResponse(data)


class AppointUpdate(LoginRequiredMixin, BSModalUpdateView):
    login_url = 'login'
    form_class = AppointmentForm
    queryset = Appointment.objects.all()
    template_name = 'meeting/edit.html'
    success_message = 'Appointment Updated Successfully'
    success_url = reverse_lazy('meeting-list')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)


class AppointList(LoginRequiredMixin, ListView):
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


class AppointSearch(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Appointment
    template_name = 'meeting/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Appointment.objects.filter(
            Q(first_Name__icontains=query) | Q(last_Name__icontains=query) | Q(NIC__istartswith=query) | Q(
                address__region__contains=query) \
            | Q(status__contains=query) | Q(address__address__istartswith=query) | Q(telephone__exact=query) \
            | Q(reasons__icontains=query)
        )
        return object_list
