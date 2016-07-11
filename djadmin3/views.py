from os.path import join

from django.conf import settings
from django.views.generic import TemplateView, ListView

from .utils import get_admin3s

ADMIN3_THEME_DIRECTORY = getattr(settings, "ADMIN3_THEME_DIRECTORY", "theme_simple_admin")


class IndexView(TemplateView):
    def get_template_names(self):
        return join(ADMIN3_THEME_DIRECTORY, "index.html")

    def get_context_data(self, **kwargs):
        if 'groups' not in kwargs:
            kwargs['groups'] = get_admin3s()
        return kwargs


class ModelListView(ListView):
    def get_template_names(self):
        return join(ADMIN3_THEME_DIRECTORY, "list.html")

        # def get_context_data(self, **kwargs):
        #     if 'groups' not in kwargs:
        #         kwargs['groups'] = get_admin3s()
        #     return kwargs
