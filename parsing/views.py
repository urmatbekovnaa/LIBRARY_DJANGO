from django.views import generic
from . import models, forms
from django.http import HttpResponse


class LitnetListView(generic.ListView):
    template_name = "parsing/litnet_list.html"
    context_object_name = "litnet"
    model = models.Parser

    def get_queryset(self):
        return models.Parser.objects.filter().order_by("-id")


class LitnetFormView(generic.FormView):
    template_name = "parsing/parsing_form.html"
    form_class = forms.ParsingForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("200 ok")
        else:
            return super(LitnetFormView, self).post(request, *args, **kwargs)
