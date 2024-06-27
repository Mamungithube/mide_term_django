# Generated by Django 5.0.6 on 2024-06-25 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.ImageField(upload_to='')),
                ('car_name', models.CharField(max_length=200)),
                ('car_price', models.IntegerField()),
                ('car_description', models.CharField(max_length=200)),
                ('Brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ManyToManyField(blank=True, to='carapp.car')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
