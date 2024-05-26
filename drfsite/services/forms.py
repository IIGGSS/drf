from django import forms

from services.models import Service, ServiceSlot


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class ServiceSlotCreateForm(forms.ModelForm):
    class Meta:
        model = ServiceSlot
        fields = ["duration", "start_time"]
