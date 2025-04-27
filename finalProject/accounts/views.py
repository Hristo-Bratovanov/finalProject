from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, TemplateView
from finalProject.accounts.forms import AppUserCreationForm, ProfileEditForm, AppUserLoginForm
from finalProject.accounts.models import Profile

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response

class AppUserLogoutView(LogoutView):
    pass

class AppUserDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())

class ProfileDetailsView(TemplateView):
    template_name = 'accounts/profile-details-page.html'

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )

class ProfileDeleteView(TemplateView):
    pass
