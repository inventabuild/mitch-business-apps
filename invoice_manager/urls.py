from django.urls import path
from . import views

urlpatterns = [
    path('invoice_view/<int:id>/', views.invoice_view, name='invoice_view'),
    path('invoice_list/', views.invoice_list, name='invoice_list'),
    path('invoice_options_list/', views.invoice_options_list, name='invoice_options_list'),
    path('invoice_new_view_edit/<int:id>/', views.invoice_new_view_edit, name='invoice_new_view_edit'),
]