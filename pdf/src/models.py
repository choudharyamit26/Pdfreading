# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.conf import settings


# class UserManager(BaseUserManager):
#
#     def create_user(self, email, password=None, **extra_fields):
#         """Creates and saves a new user"""
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, password):
#         """Creates and saves a new super user"""
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """ User model """
#     name = models.CharField(default='', max_length=100, null=True, blank=True)
#     email = models.CharField(default='', max_length=255, unique=True)
#     password = models.CharField(default='123456', max_length=100)
#     confirm_password = models.CharField(default='123456', max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserManager()
#     USERNAME_FIELD = 'email'


class DailyRenewableGenerationReport(models.Model):
    date = models.DateField(default='', null=True, blank=True, max_length=500)
    state_region = models.CharField(default='', null=True, blank=True, max_length=500)
    wind_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    solar_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    hydro_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    total = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_wind_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_solar_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_hydro_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_total = models.CharField(default='', null=True, blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class DailyRenewableGenerationReportISGS(models.Model):
    date = models.DateField(default='', blank=True, null=True, max_length=500)
    name = models.CharField(default='', null=True, blank=True, max_length=500)
    state = models.CharField(default='', null=True, blank=True, max_length=500)
    sector = models.CharField(default='', null=True, blank=True, max_length=500)
    owner = models.CharField(default='', null=True, blank=True, max_length=500)
    type = models.CharField(default='', null=True, blank=True, max_length=500)
    installed_capacity = models.CharField(default='', null=True, blank=True, max_length=500)
    actual_generation = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_generation = models.CharField(default='', null=True, blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class StateControlArea(models.Model):
    date = models.DateField(default='', blank=True, null=True, max_length=500)
    state_region = models.CharField(default='', null=True, blank=True, max_length=500)
    wind_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    solar_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    hydro_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    total = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_wind_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_solar_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_hydro_energy = models.CharField(default='', null=True, blank=True, max_length=500)
    cum_total = models.CharField(default='', null=True, blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class UserNotification(models.Model):
    """Notification model"""
    to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(default='title', max_length=200)
    body = models.CharField(default='body', max_length=200)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class CrawlCount(models.Model):
    count = models.CharField(default='', null=True, blank=True, max_length=10)
