# Generated by Django 3.0.3 on 2020-04-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0008_auto_20190819_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sweetshop',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]