from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'user {form.cleaned_data["username"]} has successfully created. Now you can Login!')
            return redirect('user-login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is wrong!')

    return render(request, 'account/login.html', context={})


def logout_view(request):
    logout(request)
    return redirect('user-login')
