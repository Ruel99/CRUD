# Generated by Django 4.2.5 on 2023-10-21 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('moblie', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=200)),
                ('person_of_intrest', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
        ),
    ]
