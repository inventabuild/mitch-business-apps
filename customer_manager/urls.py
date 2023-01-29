from django.urls import path
from . import views

urlpatterns = [
    path('customer_new/<slug:wizStatus>/', views.customer_new, name='customer_new' ),
    path('customer_view/<int:id>/<slug:wizStatus>/', views.customer_view, name='customer_view'),
    path('customer_list/<slug:wizStatus>/', views.customer_list, name='customer_list'),
    path('customer_options_list/<slug:wizStatus>/', views.customer_options_list, name='customer_options_list'),
]