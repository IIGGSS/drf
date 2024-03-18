from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Administrator)
admin.site.register(Service)
admin.site.register(Subject)
admin.site.register(Registragtion_for_service)
admin.site.register(Homework)
admin.site.register(File)
admin.site.register(New)