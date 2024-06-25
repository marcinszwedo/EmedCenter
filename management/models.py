from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

from emed import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser musi mieć is_staff=True'
            )

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser musi mieć is_superuser=True'
            )

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    pesel = models.CharField(max_length=11, null=True)

    GENDER_CHOICES = (
        ('K', 'Kobieta'),
        ('M', 'Mężczyzna'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birthdate = models.DateField(null=True)
    street = models.CharField(max_length=60, null=True)
    house_number = models.CharField(max_length=10, null=True)
    apartment_number = models.CharField(max_length=10, null=True)
    zip_code = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=9, null=True)
    main_doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    APPROVED_CHOICES = (
        (0, 'Nie zatwierdzony'),
        (1, 'Zatwierdzony'),
    )
    approved = models.IntegerField(default=0, choices=APPROVED_CHOICES, null=True)

    objects = CustomUserManager()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Specialization(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class DoctorSpecialization(models.Model):
    name = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    specialization = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Medicament(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    dose = models.CharField(max_length=40)
    quantity_in_package = models.SmallIntegerField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Order(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Zamówienie_Pacjent')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Zamówienie_Lekarz')
    order_date = models.DateField(auto_now_add=True)

    APPROVED_CHOICES = (
        (0, 'Nie zatwierdzony'),
        (1, 'Zatwierdzony'),
    )
    approved = models.IntegerField(default=0, choices=APPROVED_CHOICES)

    def __unicode__(self):
        return f'Id: {self.pk}, Pacjent: {self.patient.primary_key}, Lekarz: {self.doctor.primary_key},' \
               f'Data zamówienia: {self.order_date}, Zatwierdzone: {self.approved} '


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    lek = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()

    def __unicode__(self):
        return f'Id: {self.pk}, Zamówienie: {self.order.primary_key}, Lek: {self.lek.primary_key},' \
               f'Ilość: {self.quantity}'


class Visit(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Wizyta_Pacjent')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Wizyta_Lekarz')
    date = models.DateTimeField()

    def __unicode__(self):
        return '%s do %s (%s)' % (self.patient, self.doctor, self.date)