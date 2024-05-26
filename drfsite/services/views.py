from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, View

from subjects.models import Subject
from .forms import ServiceCreateForm, ServiceSlotCreateForm
from .models import Service, ServiceSlot


class ServiceListView(ListView):
    queryset = Service.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and hasattr(self.request.user, "tutor"):
            return qs.filter(tutor=self.request.user.tutor)
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["subjects"] = Subject.objects.all()
        return data


class ServiceCreateView(CreateView):
    queryset = Service.objects.all()
    form_class = ServiceCreateForm
    template_name = "services/service_form.html"

    def get_success_url(self):
        return reverse("service-list")


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = "services/service_detail.html"


class ServiceSlotCreateView(LoginRequiredMixin, CreateView):
    queryset = ServiceSlot.objects.all()
    form_class = ServiceSlotCreateForm

    def form_valid(self, form):
        service_pk = self.kwargs["pk"]
        self.object = form.save(commit=False)
        self.object.service = Service.objects.get(pk=service_pk)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(
            self.request,
            messages.ERROR,
            form.errors,
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("service-detail", kwargs={"pk": self.kwargs["pk"]})


class ServiceSlotSignOnView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        service_slot_pk = self.kwargs["pk"]
        service_slot = ServiceSlot.objects.get(pk=service_slot_pk)
        if hasattr(request.user, "student"):
            service_slot.student = request.user.student
            service_slot.save()
            return redirect(reverse("service-list"))
        messages.add_message(
            self.request, messages.ERROR, message="Вы должны быть студентом"
        )
        return redirect(
            reverse("service-detail", kwargs={"pk": service_slot.service_id})
        )


class ServiceSlotListView(LoginRequiredMixin, ListView):
    queryset = ServiceSlot.objects.all()
    template_name = "services/my_slots.html"

    def get_queryset(self):
        if not hasattr(self.request.user, "student"):
            messages.add_message(self.request, messages.ERROR, message="Вы не студент")
            return ServiceSlot.objects.none()
        return ServiceSlot.objects.filter(student=self.request.user.student)
