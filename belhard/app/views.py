from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Category

@require_GET
def index(request: HttpRequest, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    print(category)
    return HttpResponse('<b>HELLO</b>')


def error404(request, exception):
    return HttpResponse('404')
