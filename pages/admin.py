from django.contrib import admin

# Register your models here.
from .models import Event, Executive, ExecutiveRole, Configuration, Image, Programme, Course, Book

admin.site.register(Executive)
admin.site.register(ExecutiveRole)
admin.site.register(Configuration)
admin.site.register(Event)


admin.site.register(Programme)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(Image)