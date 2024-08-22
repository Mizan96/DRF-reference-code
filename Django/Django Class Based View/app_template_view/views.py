from typing import Any
from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class HomePage(TemplateView):
    template_name = 'templates_view/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Mizan'
        context['roll'] = 101
        # context = {
        #     'name': 'Mizan',
        #     'roll': 101
        # }
        print(context)
        print(kwargs)
        return context
