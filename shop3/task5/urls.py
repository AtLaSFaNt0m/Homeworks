from django.urls import path
from .views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('', sign_up_by_django, name='sign_up'),
    path('django_sign_up/', sign_up_by_html, name='django_sign_up'),
]
