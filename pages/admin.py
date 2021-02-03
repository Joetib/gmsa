from django.contrib import admin

# Register your models here.
from .models import Business, ContactMessage, Event, Executive, ExecutiveRole, Configuration, Image, Madarasah, MadarasahCategory, Product, Programme, Course, Book, Slider

admin.site.register(Executive)
admin.site.register(ExecutiveRole)
admin.site.register(Configuration)
admin.site.register(Event)


admin.site.register(Programme)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(Image)
admin.site.register(ContactMessage)
admin.site.register(MadarasahCategory)
admin.site.register(Madarasah)

admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Slider)