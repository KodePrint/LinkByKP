from django.shortcuts import render
from django.views.generic.list import ListView

from client.models import Branch

# Create your views here.


class ClientListView(ListView):
    model = Branch

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = 'client'
        return context