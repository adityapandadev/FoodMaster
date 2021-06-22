# Generated by Django 2.2.3 on 2019-07-17 08:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sweetshop',
            name='contact',
        ),
        migrations.AddField(
            model_name='sweetshop',
            name='phone_no',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')]),
        ),
    ]
