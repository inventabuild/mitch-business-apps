from django.urls import path
from . import views

urlpatterns = [
    path('company_options_list', views.company_options_list, name='company_options_list'),
]