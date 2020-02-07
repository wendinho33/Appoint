from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm
from django.contrib import messages


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'welcome' + ' ' + request.user.username)
                return redirect('home')
            else:
                messages.warning(request, 'please try again')
                return redirect('login')
        else:
            messages.error(request, 'form invalid')
            return redirect('login')
    else:
        form = LoginForm()
        dic = {'form': form}
        return render(request, 'account/login.html', dic)


def user_logout(request):
    logout(request)
    messages.info(request, 'you have been logout')
    return redirect('login')
