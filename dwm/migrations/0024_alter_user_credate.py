# Generated by Django 4.0.6 on 2022-08-05 02:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwm', '0023_alter_user_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 11, 21, 6, 887315)),
        ),
    ]
