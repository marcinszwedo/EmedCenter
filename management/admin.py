from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from .forms import UserCreateForm
from .models import CustomUser, Specialization, Order, Medicament, OrderDetails, Visit, DoctorSpecialization


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreateForm
    list_display = ['username', 'first_name', 'last_name', 'is_staff']


class MedicamentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    admin.site.register(CustomUser, CustomUserAdmin)
    admin.site.register(Specialization)
    admin.site.register(DoctorSpecialization)
    admin.site.register(Order)
    admin.site.register(Medicament)
    admin.site.register(OrderDetails)
    admin.site.register(Visit)
