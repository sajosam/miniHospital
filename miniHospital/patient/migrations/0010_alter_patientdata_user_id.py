# Generated by Django 4.1 on 2023-03-11 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0009_alter_patientdata_covid_vacciantion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='user_id',
            field=models.ForeignKey(limit_choices_to={'is_patient': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
