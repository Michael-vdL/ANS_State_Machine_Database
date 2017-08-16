from bin.junos_information_collector import information_collector
from bin.database_model_generator import generate_models

from django.views import generic
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Device


class IndexView(generic.ListView):
    template_name = 'juniper/index.html'
    context_object_name = 'all_devices'

    def get_queryset(self):
        return Device.objects.all()

class DevicesView(generic.ListView):
    template_name = 'juniper/devices.html'
    context_object_name = 'all_devices'

    def get_queryset(self):
        return Device.objects.all().order_by('host_name')

class DetailView(generic.DetailView):
    model = Device
    template_name = 'juniper/detail.html'

class DeviceCreate(CreateView):
    model = Device
    fields = ['host_name', 'ipv4_address', 'root_name', 'password']

class DeviceUpdate(UpdateView):
    model = Device
    fields = ['host_name', 'ipv4_address', 'root_name', 'password']

class DeviceDelete(DeleteView):
    model = Device
    success_url = reverse_lazy('juniper:devices')


def SessionOpen(request, pk):
    dev = Device.objects.get(host_name=pk)
    dev.to_python()
    #session = Device.objects.get(host_name=pk).session
    #session.open()
    #print(session.facts)
    return HttpResponse("<h1>This shit sucks</h1>")
####DEVICE/DEVICES VIEWS

