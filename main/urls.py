"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views


urlpatterns = [
 
    path('', views.main_view , name='mainview'),
    path('hawitwork/', views.hawitwork , name='hawitwork'),
    path('update-order-status/', views.update_order_status, name='update_order_status'),
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('manage-profile-or-order/', views.manage_profile_or_order, name='manage_profile_or_order'),   
    #path('charge/<int:order_id>/', views.charge, name='charge'),
   
     path('checkoutstripe/<int:order_id>/', views.checkout_view, name='checkoutstripe'),
    path('payment-success/<int:product_id>/', views.payment_success_view, name='payment_success'),
    path('payment-failed/<int:product_id>/', views.payment_cancel_view, name='payment_cancel'),
 
] 

