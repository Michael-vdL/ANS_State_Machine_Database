from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from juniper.models import Device

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'statemachine/index.html'
    context_object_name = 'all_devices'

    def get_queryset(self):
        return Device.objects.all()