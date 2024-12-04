from django.urls import path
from . import views

urlpatterns = [
    path("litnet_list/", views.LitnetListView.as_view(), name="litnet_list"),
    path("parsing_form/", views.LitnetFormView.as_view(), name="parsing_form"),
]
