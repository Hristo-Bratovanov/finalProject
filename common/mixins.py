from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views import View


class NeverCacheMixin(View):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

