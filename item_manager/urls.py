from django.urls import path
from . import views

urlpatterns = [
    path('item_new/', views.item_new, name = 'item_new'),
]