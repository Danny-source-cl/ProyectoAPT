# Generated by Django 5.1.2 on 2024-10-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panaderia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='panaderia/static/img/'),
        ),
    ]