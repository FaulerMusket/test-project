from django.contrib import admin

from .models import Lesson, Product, AccesToProduct

admin.site.register(Lesson)
admin.site.register(Product)
admin.site.register(AccesToProduct)