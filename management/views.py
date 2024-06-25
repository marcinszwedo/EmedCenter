from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, FormView, DeleteView

from management import forms
from management import models
from dal import autocomplete


class Home(View):

    def get(self, request):
        return render(request, template_name='home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Zostałeś poprawnie zalogowany'))
            return redirect('home')
        else:
            messages.success(request, ('Niepoprawne dane. Spróbuj ponownie'))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Zostałeś poprawnie wylogowany'))
    return redirect('home')


class UserCreateView(SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('home')
    template_name = 'registration/user_create.html'
    form_class = forms.UserCreateForm
    model = models.CustomUser
    success_message = 'Użytkownik został stworzony'


class UserToApprovedView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, template_name='registration/user_read.html',
                      context={'to_approved': models.CustomUser.objects.filter(approved=0, is_staff=0)})


class UserApproveUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'registration/user_update.html'
    model = models.CustomUser
    form_class = forms.UserApprovedForm
    success_url = reverse_lazy('home')
    success_message = 'Użytkownik potwierdzony'


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'registration/user_update.html'
    model = models.CustomUser
    form_class = forms.UserUpdateForm
    success_url = reverse_lazy('home')
    success_message = 'Dane zostały poprawnie zmienione.'


class MedicamentCreateView(PermissionRequiredMixin, FormView):
    template_name = 'medicament/medicament_create.html'
    form_class = forms.MedicamentForm
    success_url = reverse_lazy('medicament-read')
    permission_required = 'management.add_medicament'

    def form_valid(self, form):
        result = super().form_valid(form)

        oczyszczone_dane = form.cleaned_data
        models.Medicament.objects.create(
            name=oczyszczone_dane['name'],
            manufacturer=oczyszczone_dane['manufacturer'],
            dose=oczyszczone_dane['dose'],
            quantity_in_package=oczyszczone_dane['quantity_in_package'],
        )
        return result


class MedicamentReadView(LoginRequiredMixin, View):
    permission_required = 'management.view_medicament'

    def get(self, request):
        return render(request, template_name='medicament/medicament_read.html',
                      context={'medicament_list': models.Medicament.objects.all()})


class MedicamentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return models.Medicament.objects.none()

        qs = models.Medicament.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

            return qs


class MedicamentUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'medicament/medicament_update.html'
    model = models.Medicament
    form_class = forms.MedicamentForm
    success_url = reverse_lazy('medicament-read')
    permission_required = 'management.change_medicament'


class MedicamentDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'medicament/medicament_delete.html'
    model = models.Medicament
    success_url = reverse_lazy('medicament-read')
    permission_required = 'management.delete_medicament'


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'order/order_create.html'
    success_url = reverse_lazy('order-create')
    model = models.Order
    fields = ['patient', 'doctor']


class OrderReadDoctorView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, template_name='order/order_to_approved.html',
                      context={'order_list': models.OrderDetails.objects.filter(order_id__doctor=self.request.user
                                                                                ).filter(order_id__approved=0)})


class OrderReadView(LoginRequiredMixin, View):

    def get(self, request):
        is_approved = models.CustomUser.objects.filter(username=self.request.user).values('approved').first().get(
            'approved')
        if is_approved:
            return render(request, template_name='order/order_read.html',
                          context={'order_list': models.OrderDetails.objects.filter(order_id__patient=self.request.user
                                                                                    )})
        else:
            messages.warning(request, 'Konto musi zostać zatwierdzone.')
            return redirect('home')


class OrderUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'order/order_update.html'
    model = models.Order
    form_class = forms.OrderForm
    success_url = reverse_lazy('order-read')
    permission_required = 'management.change_order'
    success_message = 'Zamówienie zostało zmienione'


class OrderDetailsCreateForm(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'order_details/order_details_create_new.html'
    form_class = forms.OrderMultiForm
    success_url = reverse_lazy('home')
    success_message = 'Zamówienie zostało utworzone'

    def form_valid(self, form):
        is_approved = models.CustomUser.objects.filter(username=self.request.user).values('approved').first().get(
            'approved')
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        actually_user = self.request.user
        main_doctor_pk = models.CustomUser.objects.filter(username=actually_user).values('main_doctor_id').first().get(
            'main_doctor_id')
        main_doctor = models.CustomUser.objects.get(pk=main_doctor_pk)
        order = models.Order.objects.create(
            patient=actually_user,
            doctor=main_doctor,
        )

        models.OrderDetails.objects.create(
            lek=cleaned_data['lek'],
            order=order,
            quantity=cleaned_data['quantity'],
        )
        return result


class SpecializationCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.SpecializationForm
    template_name = 'specialization_create.html'
    permission_required = 'management.add_specialization'
    success_url = reverse_lazy('home')
    success_message = 'Specjalizacja została stworzona'
