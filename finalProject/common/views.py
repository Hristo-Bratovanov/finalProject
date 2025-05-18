from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView, TemplateView
from pyperclip import copy

from finalProject.common.forms import CommentForm, SearchForm
from finalProject.common.models import Like
from finalProject.projects.models import Project


class HomePage(TemplateView):
    # model = Project
    template_name = 'common/home-page.html'
    # context_object_name = 'all_project'
    # paginate_by = 10
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['comment_form'] = CommentForm()
    #     context['search_form'] = SearchForm(self.request.GET)
    #
    #     user = self.request.user
    #
    #     for project in context['all_project']:
    #         project.has_liked = project.like_set.filter(user=user).exists() if user.is_authenticated else False
    #
    #     return context


@login_required
def likes_functionality(request, project_id:int):
    liked_object = Like.objects.filter(
        to_project_id=project_id,
        user=request.user,
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_project_id=project_id, user=request.user)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{project_id}')


def share_functionality(request, project_id:int):
    copy(request.META.get('HTTP_REFERER') + resolve_url('project-details', project_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{project_id}')

@login_required
def comment_functionality(request, project_id:int):
    if request.method == 'POST':
        project = Project.objects.get(pk=project_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_project = project
            comment.user = request.user
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{project_id}')





