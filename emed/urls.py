"""
URL configuration for emed project.

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
from django.urls import path
from django.urls import re_path as url

from management import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),

    path('accounts/login/', views.login_user, name='login'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('accounts/user_create/', views.UserCreateView.as_view(), name='user-create'),
    path('accounts/user_update/<pk>', views.UserUpdateView.as_view(), name='user-update'),

    path('registration/user_read', views.UserToApprovedView.as_view(), name='user-to-approve'),
    path('registration/user_approve/<pk>', views.UserApproveUpdateView.as_view(), name='user-approve'),

    path('medicament/medicament_create/', views.MedicamentCreateView.as_view(), name='medicament-create'),
    path('medicament/medicament_read/', views.MedicamentReadView.as_view(), name='medicament-read'),
    path('medicament/medicament_update/<pk>', views.MedicamentUpdateView.as_view(), name='medicament-update'),
    path('medicament/medicament_delete/<pk>', views.MedicamentDeleteView.as_view(), name='medicament-delete'),
    url(r'^medicament-autocomplete/$', views.MedicamentAutocomplete.as_view(), name='medicament-autocomplete'),

    path('order/order_create/', views.OrderCreateView.as_view(), name='order-create'),
    path('order/order_read/', views.OrderReadView.as_view(), name='order-read'),
    path('order/order_update/<pk>', views.OrderUpdateView.as_view(), name='order-update'),
    path('order_details/order_details_create_new/', views.OrderDetailsCreateForm.as_view(), name='order-details-create-new'),
    path('order/order_to_approved/', views.OrderReadDoctorView.as_view(), name='order-to-approved'),

    path('specialization_create/', views.SpecializationCreateView.as_view(), name='specialization-create'),
]
