
from django.conf.urls import url
from . import views

app_name = 'juniper'

urlpatterns = [
    #/juniper
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/juniper/devices
    url(r'^devices/$', views.DevicesView.as_view(), name='devices'),

    #/juniper/devices/add
    url(r'^devices/add/$', views.DeviceCreate.as_view(), name='device-add'),

    # /juniper/devices/update
    url(r'^devices/(?P<pk>[aA-zZ]+[\w-]+)/update/$', views.DeviceUpdate.as_view(), name='device-update'),

    # /juniper/devices/delete
    url(r'^devices/(?P<pk>[aA-zZ]+[\w-]+)/delete/$', views.DeviceDelete.as_view(), name='device-delete'),

    #/juniper/devices/<host_name = pk>
    url(r'^devices/(?P<pk>[aA-zZ]+[\w-]+)/$', views.DetailView.as_view(), name='detail'),

    #/juniper/devices/<host_name = pk>/ssh_up
    url(r'^devices/(?P<pk>[aA-zZ]+[\w-]+)/$', views.SessionOpen, name='get-info'),

]