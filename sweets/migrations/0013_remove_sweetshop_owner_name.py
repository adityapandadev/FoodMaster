# Generated by Django 3.0.3 on 2020-04-20 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0012_sweetshop_map_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sweetshop',
            name='owner_name',
        ),
    ]
