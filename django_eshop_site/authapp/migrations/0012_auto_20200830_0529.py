# Generated by Django 3.1 on 2020-08-30 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20200830_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 1, 5, 29, 20, 421433)),
        ),
    ]