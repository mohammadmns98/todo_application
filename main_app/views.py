from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Work
from .forms import UserCreateTask


class Home(LoginRequiredMixin, ListView):
    login_url = '/users/login/'
    template_name = 'work/home.html'

    def get_queryset(self):
        return Work.objects.filter(user=self.request.user)


class CreateTaskView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    template_name = 'work/create-task.html'
    form_class = UserCreateTask

    def get_initial(self, *args, **kwargs):
        initial = super(CreateTaskView, self).get_initial()
        initial['user'] = self.request.user
        return initial


class EditTaskView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login/'
    model = Work
    template_name = 'work/edit-task.html'
    fields = ['name', 'description', 'end_date']


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login/'
    model = Work
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DoneTaskView(LoginRequiredMixin, View):
    login_url = '/users/login/'

    def get(self, request, *args, **kwargs):
        qs = Work.objects.get(id=kwargs['pk'])
        qs.status = False if qs.status else True
        qs.save()

        return redirect('home')
