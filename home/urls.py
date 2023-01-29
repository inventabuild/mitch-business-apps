from django.urls import path
from . import views

urlpatterns = [
    path('index/<slug:wizStatus>/', views.index, name='index'),
]
