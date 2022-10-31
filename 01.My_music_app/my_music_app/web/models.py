from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

MAX_LENGTH = 30
MID_LENGTH = 15
MIN_LENGTH = 2
MIN_FLOAT = 0.0
VALIDATE_USERNAME_ERROR = "Ensure this value contains only letters, numbers, and underscore."


def user_name_validation(name):
    if not all(x for x in name if x.isalpha() or x.isdigit() or x == '_'):
        raise ValidationError(VALIDATE_USERNAME_ERROR)


class Profile(models.Model):
    user_name = models.CharField(
        max_length=MID_LENGTH,
        validators=(user_name_validation,
                    MinLengthValidator(MIN_LENGTH)
                    )
    )

    e_mail = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    # Used to display the profile details in the profile details page

    @property
    def username(self):
        return f"{self.user_name}"

    @property
    def email(self):
        return f"{self.e_mail}"

    @property
    def user_age(self):
        return f"{self.age}"


class Album(models.Model):
    album_name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=MAX_LENGTH,
        choices=[("PM", "Pop Music"), ("JM", "Jazz Music"), ("RBM", "R&B Music"), ("RM", "Rock Music"),
                 ("CM", "Country Music"), ("DM", "Dance Music"), ("HHM", "Hip Hop Music"),
                 ("OM", "Other")]
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[MinValueValidator(MIN_FLOAT)]
    )

    class Meta:
        ordering = ('artist', "album_name")
