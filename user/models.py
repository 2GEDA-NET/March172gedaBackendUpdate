from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext as _
from django.conf import settings
from .managers import UserManager
from location_field.models.plain import PlainLocationField
# from django.contrib.gis.db import models as gis_models

# Create your models here.


class User(AbstractUser):
    is_business = models.BooleanField(
        default=False, verbose_name='Business Account')
    is_personal = models.BooleanField(
        default=False, verbose_name='Personal Account')
    is_admin = models.BooleanField(default=False, verbose_name='Admin Account')
    phone_number = models.BigIntegerField(unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False, verbose_name='Verified')
    # location = gis_models.PointField(null=True, blank=True)

    objects = UserManager()

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return str(self.first_name) or ''


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Rather not say', 'Rather not say'),
)


DAYS_OF_THE_WEEK_CHOICES = (
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


class BusinessCategory(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    # Create a one-to-one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=15, choices=GENDER_CHOICES, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    address = models.ForeignKey('Address', on_delete = models.CASCADE)
    

    def __str__(self):
        return self.user.username


class BusinessAvailability(models.Model):
    business = models.OneToOneField('BusinessProfile', on_delete=models.CASCADE)
    always_available = models.BooleanField(default=False)
    # Define availability for each day of the week
    # sunday
    sunday = models.BooleanField(default=False)
    sunday_open = models.TimeField(null=True, blank=True)
    sunday_close = models.TimeField(null=True, blank=True)
    # monday
    monday = models.BooleanField(default=False)
    monday_open = models.TimeField(null=True, blank=True)
    monday_close = models.TimeField(null=True, blank=True)
    # tuesday
    tuesday = models.BooleanField(default=False)
    tuesday_open = models.TimeField(null=True, blank=True)
    tuesday_close = models.TimeField(null=True, blank=True)
    # wednesday
    wednesday = models.BooleanField(default=False)
    wednesday_open = models.TimeField(null=True, blank=True)
    wednesday_close = models.TimeField(null=True, blank=True)
    # thursday
    thursday = models.BooleanField(default=False)
    thursday_open = models.TimeField(null=True, blank=True)
    thursday_close = models.TimeField(null=True, blank=True)
    # friday
    friday = models.BooleanField(default=False)
    friday_open = models.TimeField(null=True, blank=True)
    friday_close = models.TimeField(null=True, blank=True)
    # saturday
    saturday = models.BooleanField(default=False)
    saturday_open = models.TimeField(null=True, blank=True)
    saturday_close = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Availability for {self.user.username}"



class BusinessProfile(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    role = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='business_profile/', blank=True, null=True)
    business_category = models.ForeignKey(
        BusinessCategory, on_delete=models.CASCADE)
    year_founded = models.DateField(blank=True, null=True)
    address = models.ForeignKey('Address', on_delete = models.CASCADE)




class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    postal_code = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.country + ',' + self.city)


class ReportedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_banned = models.BooleanField(default=False, verbose_name='Banned')
    is_disabled = models.BooleanField(default=False, verbose_name='Disabled')
