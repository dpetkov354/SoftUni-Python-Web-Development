# Generated by Django 4.1.2 on 2022-10-28 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_level',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.FloatField(max_length=5.0, validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
    ]
