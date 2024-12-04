from django.urls import path
from . import views

urlpatterns = [
    path("", views.DeviceListView, name="device_list"),
    path("device_detail/<int:id>/", views.DeviceDetailView, name="device_detail"),
]
