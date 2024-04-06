from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Administrator)
admin.site.register(Service)
admin.site.register(Subject)
admin.site.register(RegistrationForService)
admin.site.register(Homework)
admin.site.register(File)
admin.site.register(News)