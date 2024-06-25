from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError

from management import models
from management.models import CustomUser


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password1 = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Powtórz hasło", widget=forms.PasswordInput
    )
    pesel = forms.CharField(max_length=11, label='PESEL')

    GENDER_CHOICES = (
        ('K', 'Kobieta'),
        ('M', 'Mężczyzna'),
    )
    first_name = forms.CharField(max_length=60, label='Imię')
    last_name = forms.CharField(max_length=60, label='Nazwisko')
    email = forms.CharField(max_length=60, label='Adres mailowy')
    gender = forms.ChoiceField(label='Płeć', choices=GENDER_CHOICES)
    birthdate = forms.DateField(label='Data urodzenia')
    street = forms.CharField(max_length=60, label='Ulica')
    house_number = forms.CharField(max_length=10, label='Numer domu')
    apartment_number = forms.CharField(max_length=10, label='Numer mieszkania', required=False)
    zip_code = forms.CharField(max_length=6, label='Kod pocztowy')
    city = forms.CharField(max_length=30, label='Miasto')
    phone = forms.CharField(max_length=9, label='Numer telefonu')

    class Meta:
        model = CustomUser
        fields = ['username',
                  'password1',
                  'password2',
                  'pesel',
                  'first_name',
                  'last_name',
                  'email',
                  'gender',
                  'birthdate',
                  'street',
                  'house_number',
                  'apartment_number',
                  'zip_code',
                  'city',
                  'phone'
                  ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasło nie pasuje do siebie")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    email = forms.CharField(max_length=60, label='Adres mailowy')
    street = forms.CharField(max_length=60, label='Ulica')
    house_number = forms.CharField(max_length=10, label='Numer domu')
    apartment_number = forms.CharField(max_length=10, label='Numer mieszkania', required=False)
    zip_code = forms.CharField(max_length=6, label='Kod pocztowy')
    city = forms.CharField(max_length=30, label='Miasto')
    phone = forms.CharField(max_length=9, label='Numer telefonu')
    approved = 0

    class Meta(UserChangeForm.Meta):
        model = CustomUser

        fields = ['email',
                  'street',
                  'house_number',
                  'apartment_number',
                  'zip_code',
                  'city',
                  'phone',
                  ]

    def save(self, commit=True):
        user = super().save()
        return user


class UserApprovedForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username',
                  'pesel',
                  'first_name',
                  'last_name',
                  'email',
                  'gender',
                  'birthdate',
                  'street',
                  'house_number',
                  'apartment_number',
                  'zip_code',
                  'city',
                  'phone',
                  'main_doctor',
                  'approved',
                  ]

    def save(self, commit=True):
        user = super().save()
        return user


class MedicamentForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nazwa leku')
    manufacturer = forms.CharField(max_length=100, label='Producent')
    dose = forms.CharField(max_length=40, label='Dawka')
    quantity_in_package = forms.IntegerField(label='Ilość w opakowaniu')

    class Meta:
        model = models.Medicament
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = ['approved']


class OrderDetailsForm(forms.ModelForm):

    class Meta:
        model = models.OrderDetails
        fields = ['quantity']


class OrderMultiForm(forms.Form):
    lek = forms.ModelChoiceField(models.Medicament.objects.order_by('name'))
    quantity = forms.IntegerField()


class SpecializationForm(forms.ModelForm):

    class Meta:
        model = models.Specialization
        fields = '__all__'
