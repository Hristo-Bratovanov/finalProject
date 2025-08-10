from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from accounts.forms import AppUserCreationForm, ProfileEditForm, AppUserLoginForm
from accounts.models import CompanyProfile
from common.mixins import NeverCacheMixin

UserModel = get_user_model()


class AppUserRegisterView(NeverCacheMixin, CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response


class AppUserLoginView(NeverCacheMixin, LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = CompanyProfile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class AppUserLogoutView(LogoutView):
    pass


class ProfileEditView(NeverCacheMixin, UpdateView):
    model = CompanyProfile
    form_class = ProfileEditForm
    template_name = 'accounts/company-edit-page.html'

    def test_func(self):
        profile = get_object_or_404(CompanyProfile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'company-details',
            kwargs={'pk': self.object.pk}
        )


class ProfileDetailsView(NeverCacheMixin, DetailView):
    model = UserModel
    template_name = 'accounts/company-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_projects_count'] = self.object.projects.count()
        context['total_employees_count'] = self.object.employees.count()

        return context


class ProfileDeleteView(NeverCacheMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/company-delete-page.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user == user