# Generated by Django 5.0.2 on 2024-04-03 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdata',
            name='todate',
            field=models.DateField(blank=True),
        ),
    ]