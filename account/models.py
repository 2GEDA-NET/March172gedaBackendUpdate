from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField(_("User Bio"), blank=True, null=True)
    occupation = models.CharField(_("Occupation"), max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    phone_number = models.CharField(
        _("Phone number"), max_length=20, blank=True, null=True
    )
    gender = models.CharField(
        _("Gender"),
        max_length=15,
        choices=choices.GENDER_CHOICES,
        blank=True,
        null=True,
    )
    religion = models.CharField(
        _("Religion"),
        max_length=20,
        choices=choices.RELIGION_CHOICES,
        blank=True,
        null=True,
    )
    stickers = models.ManyToManyField(to="self", verbose_name=_("Sticker"), blank=True)
    sticking = models.ManyToManyField(to="self", verbose_name=_("Sticking"), blank=True)
    cover_image = models.ImageField(
        _("Cover Image"), upload_to="cover-images", blank=True, null=True
    )
    profile_picture = models.ImageField(
        _("Profile Image"), upload_to="profile-images", blank=True, null=True
    )
    is_flagged = models.BooleanField(_("Is flagged"), default=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username or self.user.email or "-"

    @property
    def profile_image(self):
        try:
            url = self.profile_picture.url
        except ValueError:
            url = ""
        return url


class UserAddress(models.Model):
    """A model representing a user address."""

    profile = models.ForeignKey(
        to=UserProfile, verbose_name=_("Profile"), on_delete=models.CASCADE
    )
    country = models.CharField(
        _("Country"), max_length=20, default="Nigeria", blank=True, null=True
    )
    state = models.CharField(_("State"), max_length=50, blank=True, null=True)
    city = models.CharField(_("City"), max_length=50, blank=True, null=True)
    street_address = models.CharField(
        _("Street Address"), max_length=100, blank=True, null=True
    )
    zip_code = models.CharField(_("Zip Code"), max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.profile} Address"

    class Meta:
        verbose_name = _("User Address")
        verbose_name_plural = _("User Addresses")


class UserProfileMedia(models.Model):
    profile = models.ForeignKey(
        to=UserProfile, verbose_name=_("Profile"), on_delete=models.CASCADE
    )
    media_file = models.FileField(upload_to="profile-files/", blank=True, null=True)
    media_type = models.CharField(
        _("Type of media"),
        choices=choices.MEDIA_TYPES,
        max_length=20,
        blank=True,
        null=True,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)


class UserCoverImage(models.Model):
    profile = models.ForeignKey(
        to=UserProfile, verbose_name=_("Profile"), on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="cover-files/", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class UserReward(models.Model):

    class Acknowledge(models.TextChoices):
        LOGIN = ("login", "login")
        SIGNUP = ("signup", "signup")
        POST = ("post", "post")
        COMMENT = ("comment", "comment")
        CHAT = ("chat", "chat")
        STICK = ("stick", "stick")
        LIKES = ("likes", "likes")
        TIME = ("time", "time")
        COMMERCE = ("commerce", "commerce")
        LIVESTREAM = ("livestream", "livestream")
        TICKET = ("ticket", "ticket")
        STEREO = ("stereo", "stereo")

    profile = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        verbose_name=_("User Profile"),
        related_name="rewards",
    )
    acknowledge = models.CharField(
        _("Acknowledge"), choices=Acknowledge.choices, blank=True, null=True
    )
    point = models.DecimalField(_("Point"), max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.profile}"

    @property
    def balance(self):
        return 0  # TODO


class UserPhone(models.Model):
    class Category(models.TextChoices):
        IMEI = ("imei", "imei")
        SERIAL_NUMBER = ("serial_number", "serial_number")

    phone_name = models.CharField(_("Phone Name"), max_length=20)
    category = models.CharField(
        _("Category"), max_length=20, choices=Category.choices, blank=True, null=True
    )
    id_number = models.CharField(
        _("IMEI/SerialNo"), max_length=50, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.id_number
