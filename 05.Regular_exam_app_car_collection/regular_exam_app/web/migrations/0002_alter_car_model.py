# Generated by Django 4.1.2 on 2022-10-30 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
