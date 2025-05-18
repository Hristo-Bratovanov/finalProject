from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from finalProject.common.forms import CommentForm
from finalProject.projects.forms import ProjectAddForm, ProjectEditForm
from finalProject.projects.models import Project


class ProjectAddView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectAddForm
    template_name = 'projects/project-add-page.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.user = self.request.user

        return super().form_valid(form)


class ProjectDetailsView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()
        self.object.has_liked = self.object.like_set.filter(user=self.request.user).exists()

        return context


class ProjectEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectEditForm
    template_name = 'projects/project-edit-page.html'

    def test_func(self):
        project = get_object_or_404(Project, slug=self.kwargs['pk'])
        return self.request.user == project.user

    def get_success_url(self):
        return reverse_lazy('project-details', kwargs={'pk': self.object.pk})


@login_required
def project_delete(request, pk: int):
    project = Project.objects.get(pk=pk)

    if request.user == project.user:
        project.delete()

    return redirect('home')