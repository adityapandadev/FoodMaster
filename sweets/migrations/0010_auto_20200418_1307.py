# Generated by Django 3.0.3 on 2020-04-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0009_auto_20200418_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sweetshop',
            name='adress',
        ),
        migrations.AddField(
            model_name='sweetshop',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
