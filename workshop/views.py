from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django import template

from .models import State, Transition, Routine


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'workshop/index.html'
    context_object_name = 'all_states'

    def get_queryset(self):
        return State.objects.all()

class StateCreate(CreateView):
    model = State
    fields = ['state_name', 'state_type', 'state_routines', 'state_transitions']

    success_url = reverse_lazy('workshop:index')

class StateUpdate(UpdateView):
    model = State
    fields = ['state_name', 'state_type']

class StateDelete(DeleteView):
    model = State
    success_url = reverse_lazy('workshop:index')
