# Generated by Django 5.0.6 on 2024-06-27 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0003_car_quantity_alter_car_car_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchese_date', models.DateTimeField(auto_now_add=True)),
                ('net_quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapp.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]