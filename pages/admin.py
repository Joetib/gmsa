from django.contrib import admin

# Register your models here.
from .models import Event, Executive, ExecutiveRole, Configuration

admin.site.register(Executive)
admin.site.register(ExecutiveRole)
admin.site.register(Configuration)
admin.site.register(Event)