from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='/'),
    path('quartos/', views.page_quartos, name='page_quartos')
]
