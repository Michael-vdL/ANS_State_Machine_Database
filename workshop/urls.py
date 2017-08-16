from django.conf.urls import url
from . import views

app_name = 'workshop'

urlpatterns = [
    #/workshop
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^state/add$', views.StateCreate.as_view(), name='state-add'),
    url(r'^state/(?P<pk>[aA-zZ0-9_ ]+)/update$', views.StateUpdate.as_view(), name='state-update'),
    url(r'^state/(?P<pk>[aA-zZ0-9_ ]+)/delete$', views.StateDelete.as_view(), name='state-delete')
    ]
