# Generated by Django 4.2.16 on 2024-11-29 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_appoinmentmodels_pat_name'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appoinmentmodels_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Patient.appoinmentmodels')),
            ],
            bases=('Patient.appoinmentmodels',),
        ),
    ]
