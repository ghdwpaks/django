# Generated by Django 4.0.2 on 2022-08-16 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwm', '0041_alter_user_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 18, 34, 42, 746134)),
        ),
    ]
