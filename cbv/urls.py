from django.urls import path
from . import views


urlpatterns = [
    path('order_class/', views.OrderListView.as_view(), name='order_class_list'),
    path('order_class/<int:id>/update', views.UpdateOrderView.as_view(), name='update_class_list'),
    path('order_class/<int:id>/delete', views.DeleteOrderView.as_view(), name='delete_class_list'),
    path('create_order/', views.OrderListView.as_view(), name='create_class_list'),
]