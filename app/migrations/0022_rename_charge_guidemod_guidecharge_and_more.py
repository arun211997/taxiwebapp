# Generated by Django 5.0.2 on 2024-05-06 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rename_tcharge_tollcharge_toll_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guidemod',
            old_name='charge',
            new_name='guidecharge',
        ),
        migrations.RenameField(
            model_name='guidemod',
            old_name='placw',
            new_name='place',
        ),
    ]