from django.urls import path
from . import views

urlpatterns = [
    path('', views.turismo),
    path('Brasil/', views.brasil),
    path('Italia/', views.italia),
    path('Alemanha/', views.alemanha),
]