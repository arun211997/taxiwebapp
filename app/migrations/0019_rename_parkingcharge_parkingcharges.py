# Generated by Django 5.0.2 on 2024-05-03 08:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_rename_othercharge_othercharges'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='parkingcharge',
            new_name='parkingcharges',
        ),
    ]
