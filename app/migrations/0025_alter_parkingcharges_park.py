# Generated by Django 5.0.2 on 2024-05-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_parkingcharges_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingcharges',
            name='park',
            field=models.TextField(),
        ),
    ]
