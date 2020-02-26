from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from meeting.models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import Todo
from home.forms import TodoForm
from bootstrap_modal_forms.generic import BSModalDeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required(login_url='login')
def IndexView(request):
    todo_list = Todo.objects.get_queryset().order_by('-created_at')
    page = request.GET.get('page', 1)

    paginator = Paginator(todo_list, 5)
    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        todos = paginator.page(1)
    except EmptyPage:
        todos = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Agenda updated')
            form.save()
            return redirect('home')
        else:
            messages.warning(request, 'please verify input')
            return redirect('home')
    else:
        form = TodoForm
        page = {
            'form': form,
            'lists': todo_list,
            'page_obj': todos,
            'appointment': Appointment.objects.all().order_by('-published')[:3]
        }
        return render(request, 'home/index.html', page)


class Todo_Delete(LoginRequiredMixin, BSModalDeleteView):
    login_url = 'login'
    model = Todo
    template_name = 'home/delete.html'
    queryset = Todo.objects.all()
    success_message = 'Successfully Deleted'
    success_url = reverse_lazy('home')


class TodoUpdate(UpdateView, LoginRequiredMixin):
    login_url = 'login'
    template_name = 'home/update.html'
    form_class = TodoForm
    queryset = Todo.objects.all()
    success_url = reverse_lazy('home')


class UsersView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = User
    template_name = 'home/users.html'
    queryset = User.objects.all()
    context_object_name = 'users'


@login_required(login_url='login')
def get_data(request, *args, **kwargs):
    if request.user.is_superuser:
        qs = Appointment.objects.all().count()
        data = {'meetings': qs}
        return JsonResponse(data, safe=False)
