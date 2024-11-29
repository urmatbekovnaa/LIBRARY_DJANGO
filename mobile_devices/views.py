from django.shortcuts import render, get_object_or_404
from .models import Device, Category

def DeviceListView(request):
    category_id = request.GET.get('category')
    if category_id:
        devices = Device.objects.filter(category_id=category_id)
    else:
        devices = Device.objects.all()
    categories = Category.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices,
                                                        'categories': categories})

def DeviceDetailView(request, id):
    device = get_object_or_404(Device, id=id)
    return render(request, 'devices/device_detail.html', {'device': device})
