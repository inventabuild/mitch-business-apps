from django.urls import path
from . import views

urlpatterns = [
    path('company_options_list', views.company_options_list, name='company_options_list'),
    path('company_new', views.company_new, name='company_new'),
]