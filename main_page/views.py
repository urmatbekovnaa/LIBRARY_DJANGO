from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class SearchView(generic.ListView):
    template_name = "book.html"
    context_object_name = "book_list"
    paginate_by = 5

    def get_queryset(self):
        return models.Books.objects.filter(
            title__icontains=self.request.GET.get("q")
        ).order_by("-id")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class BookListView(generic.ListView):
    template_name = "book.html"
    context_object_name = "book_list"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.select_related().order_by("-id")


class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"
    context_object_name = "book_id"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)


# def book_list_view(request):
#     if request.method == 'GET':
#         book_list = models.Books.objects.filter().order_by('-id')
#         context = {'book_list': book_list}
#         return render(request, template_name='book.html', context=context)
#
# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id)
#         context = {'book_id': book_id}
#         return render(request, template_name='book_detail.html', context=context)
