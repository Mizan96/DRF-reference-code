from typing import Any
from django.shortcuts import render

from django.views.generic.base import TemplateView, RedirectView

# Create your views here.

class NewSite(RedirectView):
    url = 'http://mizan98.pythonanywhere.com/'

class NewSite2(RedirectView):
    pattern_name = 'home3'
    permanent = True
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        print(args)
        return super().get_redirect_url(*args, **kwargs)