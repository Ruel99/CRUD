# Generated by Django 4.2.5 on 2023-10-21 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_department_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='moblie',
            new_name='mobile',
        ),
    ]