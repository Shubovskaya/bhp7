from django.urls import path, register_converter, re_path
from .views import ProductView

urlpatterns = [
    path('', ProductView.as_view()),
]
