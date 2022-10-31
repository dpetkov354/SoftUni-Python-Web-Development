from enum import unique
from django.core import validators
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE = 12
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15
    MAX_LEN_PASSWORD_AND_NAME = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
            ),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASSWORD_AND_NAME,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_PASSWORD_AND_NAME,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_PASSWORD_AND_NAME,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )


class Game(models.Model):
    MAX_LEN_CAT = 15
    MAX_LEN_NAME = 30
    MAX_LEN_RATING = 5.0
    ACTION_GAME = "Action"
    ADVENTURE_GAME = "Adventure"
    PUZZLE_GAME = "Puzzle"
    STRATEGY_GAME = "Strategy"
    SPORTS_GAME = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER_GAME = "Other"

    TYPES = (
        (ACTION_GAME, ACTION_GAME),
        (ADVENTURE_GAME, ADVENTURE_GAME ),
        (PUZZLE_GAME, PUZZLE_GAME),
        (STRATEGY_GAME, STRATEGY_GAME),
        (SPORTS_GAME, SPORTS_GAME),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER_GAME , OTHER_GAME),

    )

    title = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_CAT,
        choices=TYPES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        max_length=MAX_LEN_RATING,
        validators=[MinValueValidator(0.1)]
    )

    max_level = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

