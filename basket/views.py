from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Order
from .forms import OrderForm
from django.contrib import messages


def create_order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data["book"]
            if book.stock_count > 0:
                book.reduce_stock()
                form.save()
                messages.success(request, "Заказ успешно создан!")
                return redirect("order_list")
            else:
                messages.error(request, "Извините, этой книги нет в наличии.")
    else:
        form = OrderForm()
    return render(request, "basket/create_order.html", {"form": form})


# Просмотр списка заказов
def order_list_view(request):
    orders = Order.objects.all()
    return render(request, "basket/order_list.html", {"orders": orders})


# Редактирование заказа
def update_order_view(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Заказ обновлен!")
            return redirect("order_list")
    else:
        form = OrderForm(instance=order)
    return render(request, "basket/update_order.html", {"form": form, "order": order})


# Удаление заказа
def delete_order_view(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.success(request, "Заказ удален!")
    return redirect("order_list")


# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from .models import Order
# from .forms import OrderForm
# from . import forms
# from django.contrib import messages
#
#
# def create_order_view(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Заказ успешно создан!')
#     else:
#         form = forms.OrderForm()
#     return render(request, 'basket/create_order.html', {'form': form})
#
# def order_list_view(request):
#     orders = Order.objects.filter().order_by('-id')
#     return render(request, 'basket/order_list.html', {'orders_list': orders})
#
# def delete_order_view(request, id):
#     order = get_object_or_404(Order, id=id)
#     order.delete()
#     messages.success(request, 'Заказ удален!')
#     return redirect('order_list')
#
#
# def update_order_view(request, id):
#     order = get_object_or_404(Order, id=id)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Заказ обновлен!')
#             return redirect('order_list')
#     else:
#         form = OrderForm(instance=order)
#     return render(request, 'basket/update_order.html', {'form': form, 'order': order})
#
