# Generated by Django 5.0.2 on 2024-04-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_tripdata_advance_alter_tripdata_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdata',
            name='fromdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tripdata',
            name='todate',
            field=models.DateField(null=True),
        ),
    ]
