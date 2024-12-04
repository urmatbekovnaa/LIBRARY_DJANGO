from django.urls import path
from . import views

urlpatterns = [
    path("order_list/", views.order_list_view, name="order_list"),
    path("create_order/", views.create_order_view, name="create_order"),
    path(
        "update_order/update_order/<int:id>/",
        views.update_order_view,
        name="update_order",
    ),
    path("delete_order/<int:id>/", views.delete_order_view, name="delete_order"),
]
