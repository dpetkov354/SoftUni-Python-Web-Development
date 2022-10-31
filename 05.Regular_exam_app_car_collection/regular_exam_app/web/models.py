from django.core import validators
from django.db import models
from regular_exam_app.web.validators import validate_min_length, validate_year

MAX_LENGTH = 30
MID_LENGTH = 10
MIN_LENGTH = 2
MIN_FLOAT = 0.0
MIN_AGE = 18
MAX_MODEL_LENGTH = 20
MAX_YEAR = 2049
MIN_YEAR = 1980
MIN_PRICE = 1.0

SPORTS_CAR = 'Sports Car'
PICK_UP = "Pickup"
CROSS_OVER = "Crossover"
MINI_BUS = "Minibus"
OTHER_CAR = "Other"


class Profile(models.Model):
    user_name = models.CharField(
        null=False,
        blank=False,
        max_length=MID_LENGTH,
        validators=(
            validate_min_length,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
            ),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    CARS = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICK_UP, PICK_UP),
        (CROSS_OVER, CROSS_OVER),
        (MINI_BUS, MINI_BUS),
        (OTHER_CAR, OTHER_CAR),
    )

    type = models.CharField(
        max_length=MID_LENGTH,
        choices=CARS,
        null=False,
        blank=False,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_MODEL_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH),
        )

    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validate_year,
        )
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        ),

    )
