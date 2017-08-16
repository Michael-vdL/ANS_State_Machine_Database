from django.db import models
from django.core.urlresolvers import reverse
from jsonfield import JSONField

# Create your models here.

class Transition(models.Model):
    transition_name = models.CharField(max_length=25, unique=True, primary_key=True)
    transition_destination = models.CharField(max_length=25)
    transition_security = models.BooleanField(default=False) #True if need authorization

class Routine(models.Model):
    routine_name = models.CharField(max_length=25, unique=True, primary_key=True)
    routine_description = models.CharField(max_length=1000)
    routine_type = models.CharField(max_length=6)
    #routine_triggers = JSONField() #List of Configuration or Alerts that cause routine to start
    #routine_variables = JSONField() #List of Important Variables to Track for Routine
    #routine_actions = JSONField() #List of Actionst to take
    #remember to set up a success or failure messege system or a way to trigger something else


class State(models.Model):
    state_name = models.CharField(max_length=25, unique=True, primary_key=True)
    state_type = models.CharField(max_length=6)
    state_routines = models.ManyToManyField(Transition) #Should be List of Routines State Has Access to (by name)
    state_transitions = models.ManyToManyField(Routine) #Should be a list of Transitions the State Has access too (by name)

    def get_absolute_url(self):
        return reverse('workshop:index', kwargs={'pk': self.pk})
