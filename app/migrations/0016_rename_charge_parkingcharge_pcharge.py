# Generated by Django 5.0.2 on 2024-05-01 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_parkingcharge_charge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkingcharge',
            old_name='charge',
            new_name='pcharge',
        ),
    ]
