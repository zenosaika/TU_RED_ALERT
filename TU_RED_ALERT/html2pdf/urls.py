from django.urls import path
from . import views

urlpatterns = [
    path('', views.html2pdf, name='html2pdf'),
]