from django.urls import path
from . import views

urlpatterns = [
    path('customer_pricing_new/', views.customer_pricing_new, name='customer_pricing_new'),
    path('customer_pricing_view/<int:id>', views.customer_pricing_view, name='customer_pricing_view'),
    path('customer_pricing_list/', views.customer_pricing_list, name='customer_pricing_list'),
    path('customer_pricing_options_list/', views.customer_pricing_options_list, name='customer_pricing_options_list'),
]