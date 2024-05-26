from django.urls import path

from .views import (
    ServiceListView,
    ServiceCreateView,
    ServiceDetailView,
    ServiceSlotCreateView,
    ServiceSlotSignOnView,
    ServiceSlotListView,
)

urlpatterns = [
    path("", ServiceListView.as_view(), name="service-list"),
    path("create", ServiceCreateView.as_view(), name="service-create"),
    path("detail/<pk>", ServiceDetailView.as_view(), name="service-detail"),
    path(
        "slot/<pk>/create", ServiceSlotCreateView.as_view(), name="service-slot-create"
    ),
    path(
        "slot/<pk>/sign-on",
        ServiceSlotSignOnView.as_view(),
        name="service-slot-sign-on",
    ),
    path(
        "my-slots",
        ServiceSlotListView.as_view(),
        name="my-slots",
    ),
]
