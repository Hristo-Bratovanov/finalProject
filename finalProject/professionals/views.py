from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from finalProject.common.forms import CommentForm
from finalProject.professionals.forms import ProfessionalAddForm, ProfessionalEditForm, ProfessionalDeleteForm
from finalProject.professionals.models import Professional


class ProfessionalAddPage(LoginRequiredMixin, CreateView):
    model = Professional
    form_class = ProfessionalAddForm
    template_name = 'professionals/professional-add-page.html'

    def form_valid(self, form):
        professional = form.save(commit=False)
        professional.user = self.request.user
        return super().form_valid()

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk
            }
        )

class ProfessionalDetailsPage(LoginRequiredMixin, DetailView):
    model = Professional
    template_name = 'professionals/professional-details-page.html'
    slug_url_kwarg = 'professional_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = context['professional'].photo_set.all()
        context['comment_form'] = CommentForm()

        all_photos = context['professional'].photo_set.all()

        for photo in all_photos:
            photo.has_liked = photo.like_set.filter(user=self.request.user).exists()

        context['all_photos'] = all_photos

        return context


class ProfessionalEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Professional
    form_class = ProfessionalEditForm
    template_name = 'professionals/professional-edit-page.html'

    def test_func(self):
        professional = get_object_or_404(Professional, slug=self.kwargs['professional_slug'])
        return self.request.user == professional.user

    def get_success_url(self):
        return reverse_lazy(
            'professional-details',
            kwargs={
                'username': self.kwargs['username'],
                'professional_slug': self.kwargs['professional_slug'],
            }
        )

class ProfessionalDeletePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Professional
    form_class = ProfessionalDeleteForm
    template_name = 'professionals/professional-delete-page.html'
    slug_url_kwarg = 'professional_slug'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk,
            }
        )

    def test_func(self):
        professional = get_object_or_404(Professional, slug=self.kwargs['professional_slug'])
        return self.request.user == professional.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs