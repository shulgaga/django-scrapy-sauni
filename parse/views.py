from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, LoginUserForm
from .models import OldInfo, NewInfo
from .filters import InfoFilter, UnsortedFilter
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class InfoListView(LoginRequiredMixin, ListView):
    model = NewInfo
    template_name = 'parse/index.html'
    login_url = 'login'
    redirect_field_name = ''
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = InfoFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return InfoFilter(self.request.GET, queryset=queryset).qs


class UnsortedListView(LoginRequiredMixin, ListView):
    model = OldInfo
    template_name = 'parse/unsorted.html'
    login_url = 'login'
    redirect_field_name = ''
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = UnsortedFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UnsortedFilter(self.request.GET, queryset=queryset).qs


def one_item_detail(request, id):
    item = get_object_or_404(NewInfo, id=id)
    return render(request, 'parse/detail.html', {'item': item})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'parse/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'parse/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')
