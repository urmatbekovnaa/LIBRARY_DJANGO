from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class SalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            level = request.POST.get("level")
            if level == "Junior":
                request.salary = 300
            elif level == "Middle":
                request.salary = 1000
            elif level == "Senior":
                request.salary = 2000
            else:
                return HttpResponseBadRequest("Некорректный уровень квалификации")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "salary", "Уровень не определен.")
