from django.contrib import admin
from .models import Service, ServiceSlot


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceSlot)
class ServiceSlotAdmin(admin.ModelAdmin):
    pass
