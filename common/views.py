from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy

from accounts.models import CompanyProfile
from common.forms import CommentForm
from common.mixins import NeverCacheMixin
from project_pictures.models import ProjectPicture
from projects.models import Project


class HomePage(NeverCacheMixin, ListView):
    model = Project
    template_name = 'common/home-page.html'
    context_object_name = 'all_projects'
    paginate_by = 3

class CompanyList(NeverCacheMixin, ListView):
    model = CompanyProfile
    template_name = 'common/companies-anonymous.html'
    context_object_name = 'companies'

    def get_queryset(self):
        return CompanyProfile.objects.filter(user__is_superuser=False)

def share_functionality(request, photo_id: int):
    picture_url = request.build_absolute_uri(resolve_url('picture-details', photo_id))
    copy(picture_url)

    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(f'{referer.split("#")[0]}#{photo_id}')

@login_required
def comment_functionality(request, photo_id: int):
    if request.method == 'POST':
        photo = ProjectPicture.objects.get(pk=photo_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')





