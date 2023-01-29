from django.urls import path
from . import views

urlpatterns = [
    path('company_options_list/<slug:wizStatus>/', views.company_options_list, name='company_options_list'),
    path('company_new/<slug:wizStatus>/', views.company_new, name='company_new'),
    path('company_view/<int:id>/<slug:wizStatus>/', views.company_view, name='company_view'),
    path('company_list/<slug:wizStatus>/', views.company_list, name='company_list'),
]