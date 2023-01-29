from django.urls import path
from . import views

urlpatterns = [
    path('customer_pricing_new/<slug:wizStatus>/', views.customer_pricing_new, name='customer_pricing_new'),
    path('customer_pricing_view/<int:id>/<slug:wizStatus>/', views.customer_pricing_view, name='customer_pricing_view'),
    path('customer_pricing_list/<slug:wizStatus>/', views.customer_pricing_list, name='customer_pricing_list'),
    path('customer_pricing_options_list/<slug:wizStatus>/', views.customer_pricing_options_list, name='customer_pricing_options_list'),
]