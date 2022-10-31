from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        verbose_name="First Name",
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    profile_image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Image URL",
    )


class Book(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    book_image_url = models.URLField(
        blank=False,
        null=False,
    )

    type = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
