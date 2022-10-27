from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Category, Product
from .forms import CalculateForm, ContactForm


class IndexView(View):

    template_name = 'app/index.html'

    def get_context_data(self):
        categories = Category.objects.all().order_by('name')
        products = Product.objects.filter(is_published=1).order_by('title')
        content = {
            'categories': categories,
            'products': products,
            'contact_form': ContactForm,
            'contact_error': None
        }
        return content

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        content = self.get_context_data()
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            content['contact_error'] = 'Error'
        return render(request, self.template_name, content)


class ProductView(ListView):
    model = Category
    template_name = 'app/index.html'
    context_object_name = 'products'
    object_list = None

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(ProductView, self).get_context_data()
        categories = Category.objects.all().order_by('name')
        content.update({
        'categories': categories,
        'contact_form': ContactForm,
        'contact_error': None
        })
        return content

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('category')

    def post(self, request):
        form = ContactForm(request.POST)
        content = self.get_context_data()
        content['products'] = self.get_queryset()
        if form.is_valid():
            form.save()
        else:
            content['contact_error'] = 'error'
        return render(request, self.template_name, content)



# def index(request: HttpRequest):
#     error = None
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error = 'Ошибка'
#     form = ContactForm()
#     categories = Category.objects.all().order_by('name')
#     products = Product.objects.filter(is_published=1).order_by('title')
#     return render(
#         request,
#         'app/index.html',
#         {
#             'categories': categories,
#             'products': products,
#             'contact_form': form,
#             'contact_error': error
#         }
#     )
#
#
def error404(request, exception):
    return HttpResponse('<b>404<b>')
#
#
# def calculate(request):
#     result = None
#     form = CalculateForm()
#     if request.method == 'POST':
#         form = CalculateForm(request.POST)
#         result = int(request.POST.get('width')) * int(request.POST.get('height'))
#     return render(request, 'app/calculate.html', {
#         'calculate_form': form,
#         'result': result
#     })


