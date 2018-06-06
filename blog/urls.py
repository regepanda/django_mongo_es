from django.urls import path
from .controller import ProductController

urlpatterns = [
    # ex: /blog/
    path('', ProductController.index, name='index'),
    # ex: /blog/5/
    path('<int:question_id>/', ProductController.detail, name='detail'),
]