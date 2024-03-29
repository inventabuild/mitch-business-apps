"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_init.urls')),
    path('home/', include('home.urls')),
    path('company_manager/', include('company_manager.urls')),
    path('item_manager/', include('item_manager.urls')),
    path('customer_manager/', include('customer_manager.urls')),
    path('customer_pricing_manager/', include('customer_pricing_manager.urls')),
    path('invoice_manager/', include('invoice_manager.urls')),
    path('blog/', include('blog.urls')),
]


