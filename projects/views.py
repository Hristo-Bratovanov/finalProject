from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.forms import CommentForm
from common.mixins import NeverCacheMixin
from projects.forms import ProjectAddForm, ProjectEditForm, ProjectDeleteForm
from projects.models import Project


class ProjectAddView(NeverCacheMixin, LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectAddForm
    template_name = 'projects/project-add-page.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'company-details',
            kwargs={
                'pk': self.request.user.pk
            }
        )


class ProjectDetailsView(NeverCacheMixin, DetailView):
    model = Project
    template_name = 'projects/project-details-page.html'
    slug_url_kwarg = 'project_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = context['project'].pictures.all()
        context['comment_form'] = CommentForm()

        all_photos = context['project'].pictures.all()

        for photo in all_photos:
            if self.request.user.is_authenticated:
                photo.has_liked = photo.like_set.filter(user=self.request.user).exists()
            else:
                photo.has_liked = False

        context['all_photos'] = all_photos
        return context


class ProjectEditView(NeverCacheMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectEditForm
    template_name = 'projects/project-edit-page.html'
    slug_url_kwarg = 'project_slug'

    def test_func(self):
        project = get_object_or_404(Project, slug=self.kwargs['project_slug'])
        return self.request.user == project.user

    def get_success_url(self):
        return reverse_lazy(
            'project-details',
            kwargs={
                'project_slug': self.kwargs['project_slug'],
            }
        )


class ProjectDeleteView(NeverCacheMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    form_class = ProjectDeleteForm
    template_name = 'projects/project-delete-page.html'
    slug_url_kwarg = 'project_slug'

    def get_success_url(self):
        return reverse_lazy(
            'company-details',
            kwargs={
                'pk': self.request.user.pk,
            }
        )

    def test_func(self):
        project = get_object_or_404(Project, slug=self.kwargs['project_slug'])
        return self.request.user == project.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs