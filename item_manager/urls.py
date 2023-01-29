from django.urls import path
from . import views

urlpatterns = [
    path('item_options_list/<slug:wizStatus>/', views.item_options_list_wizard, name = 'item_options_list'),
    path('item_new/<slug:wizStatus>/', views.item_new_wizard, name = 'item_new'),
    path('item_view/<int:id>/<slug:wizStatus>/', views.item_view_wizard, name = 'item_view'),
    path('item_list/<slug:wizStatus>/', views.item_list_wizard, name = 'item_list')
]