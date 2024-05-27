from django import forms
from django.forms import Textarea

from services.models import Service, ServiceSlot


class ServiceCreateForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ["subject", "info_about_service", "price", "level"]


class ServiceSlotCreateForm(forms.ModelForm):

    class Meta:
        model = ServiceSlot
        fields = ["duration", "start_time"]
