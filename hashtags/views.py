from django.shortcuts import render
from . import models

def all_hashtags_view(request):
    if request.method == 'GET':
        hashtags_list = models.Hashtag.objects.filter().order_by('-id')
        context = {'hashtags_list': hashtags_list}
        return render(request, 'all_hashtags.html', context=context)


def grand_list_view(request):
    if request.method == 'GET':
        grand = models.Hashtag.objects.filter(tags__name='для стариков').order_by('-id')
        context = {'grand': grand}
        return render(request, 'grand.html', context=context)

def young_list_view(request):
    if request.method == 'GET':
        young = models.Hashtag.objects.filter(tags__name='для взрослых').order_by('-id')
        context = {'young': young}
        return render(request, 'young.html', context=context)

def children_list_view(request):
    if request.method == 'GET':
        children = models.Hashtag.objects.filter(tags__name='для детей').order_by('-id')
        context = {'children': children}
        return render(request, 'children.html', context=context)