# Generated by Django 5.0.2 on 2024-04-03 02:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tripnumber', models.TextField(default='TRIP000')),
            ],
        ),
        migrations.CreateModel(
            name='tripdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tripnumber', models.TextField(null=True)),
                ('drivername', models.TextField(null=True)),
                ('guestname', models.TextField(null=True)),
                ('fromdate', models.TextField()),
                ('todate', models.TextField()),
                ('start', models.TextField(null=True)),
                ('end', models.TextField(default=0)),
                ('startkm', models.TextField(null=True)),
                ('endkm', models.TextField(default=0)),
                ('vehiclename', models.TextField(null=True)),
                ('vehiclenumber', models.TextField(null=True)),
                ('parking', models.TextField(default=0)),
                ('toll', models.TextField(default=0)),
                ('tripkm', models.TextField(default=0)),
                ('total', models.TextField(default=0)),
                ('advance', models.TextField(default=0)),
                ('balance', models.TextField(default=0)),
                ('fixed', models.TextField(null=True)),
                ('extra', models.TextField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
