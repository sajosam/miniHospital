# Generated by Django 4.1 on 2023-03-25 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_alter_account_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 3, 25)),
        ),
    ]
