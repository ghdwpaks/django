# Generated by Django 4.0.6 on 2022-08-19 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwm', '0061_alter_user_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 22, 43, 41, 303346)),
        ),
    ]
