# Generated by Django 5.0.2 on 2024-05-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_rename_pcharge_parkingcharges_zcharge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tollcharge',
            old_name='tcharge',
            new_name='toll',
        ),
        migrations.RemoveField(
            model_name='parkingcharges',
            name='zcharge',
        ),
        migrations.AddField(
            model_name='parkingcharges',
            name='park',
            field=models.TextField(null=True),
        ),
    ]
