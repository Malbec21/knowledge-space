from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phone_field import PhoneField

from src.apps.accounts.managers import CustomUserManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]


class WorkPlace(models.Model):
    name = models.CharField(max_length=128)
    image = models.FileField(blank=True, null=True, default="default_place_of_work.png")
    country = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    street = models.CharField(max_length=64, blank=True)
    phone_number = PhoneField(blank=True, help_text="Contact phone number")

    def __str__(self):
        return self.name


class User(BaseUser):
    avatar = models.FileField(blank=True, null=True, default="default_avatar.png")
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    patronymic_name = models.CharField(max_length=64, blank=True)
    place_of_work = models.ManyToManyField(
        WorkPlace, related_name="employees", blank=True
    )
    position = models.CharField(max_length=64, blank=True)
    academic_status = models.CharField(max_length=64, blank=True)
    scientific_degree = models.CharField(max_length=64, blank=True)

    objects = CustomUserManager()

    @property
    def public_name(self):
        try:
            return f"{self.first_name.capitalize()} {self.last_name[0].upper()}."
        except IndexError:
            return f"User ({self.pk})"

    def __str__(self):
        return self.public_name

    @property
    def is_filled(self):
        return (
            self.email
            and self.first_name
            and self.last_name
            and self.patronymic_name
            and self.place_of_work
            and self.position
            and self.academic_status
            and self.scientific_degree
        )
