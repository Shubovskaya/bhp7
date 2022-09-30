from django.urls import path, register_converter, re_path
from .views import index



class YearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'yyyy')


urlpatterns = [
    path('<int:category_id>', index),
]
