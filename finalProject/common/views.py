from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'common/home-page.html'

class NavPage(TemplateView):
    template_name = 'common/nav.html'


