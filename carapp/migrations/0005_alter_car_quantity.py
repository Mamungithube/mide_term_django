# Generated by Django 5.0.6 on 2024-06-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_paymentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
    ]
