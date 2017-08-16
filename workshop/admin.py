from django.contrib import admin
from .models import State, Transition, Routine

# Register your models here.
admin.site.register(State)
admin.site.register(Transition)
admin.site.register(Routine)