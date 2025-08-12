from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, UpdateView

from common.forms import CommentForm
from common.mixins import NeverCacheMixin
from project_pictures.forms import PictureAddForm, PictureEditForm
from project_pictures.models import ProjectPicture
from projects.models import Project


class PictureAddView(NeverCacheMixin, LoginRequiredMixin, CreateView):
    model = ProjectPicture
    form_class = PictureAddForm
    template_name = 'project_pictures/picture-add-page.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['project'].queryset = Project.objects.filter(user=self.request.user)
        return form

    def get_success_url(self):
        return reverse_lazy(
            'company-details',
            kwargs={
                'pk': self.request.user.pk
            }
        )

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        return super().form_valid(form)


class PictureDetailsView(NeverCacheMixin, LoginRequiredMixin, DetailView):
    model = ProjectPicture
    template_name = 'project_pictures/picture-details-page.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()

        return context


class PictureEditView(NeverCacheMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProjectPicture
    form_class = PictureEditForm
    template_name = 'project_pictures/picture-edit-page.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['project'].queryset = Project.objects.filter(user=self.request.user)
        return form

    def test_func(self):
        photo = get_object_or_404(ProjectPicture, pk=self.kwargs['pk'])
        return self.request.user == photo.user

    def get_success_url(self):
        return reverse_lazy('picture-details', kwargs={'pk': self.object.id})


@login_required
def picture_delete(request, pk: int):
    picture = get_object_or_404(ProjectPicture, pk=pk)

    if request.user == picture.user:
        picture.delete()

    return redirect('home')