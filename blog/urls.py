from django.urls import path
from .controller import ProductController, TestController

urlpatterns = [
    # ex: /blog/product/
    path('product/', ProductController.index, name='index'),
    # ex: /blog/product/5/
    path('product/<int:question_id>/', ProductController.detail, name='detail'),

    # ex: /blog/test/
    path('test/', TestController.index, name='index')
]