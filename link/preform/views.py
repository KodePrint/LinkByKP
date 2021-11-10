from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from preform.models import Branch, Preform

# Create your views here.

class PreformCreateView(CreateView):
    model = Preform
    fields = '__all__'
    success_url = reverse_lazy('customersList')

class PreformListView(ListView):
    model = Preform