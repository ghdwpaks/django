# Generated by Django 4.0.6 on 2022-08-05 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwm', '0020_alter_user_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 10, 46, 12, 881420)),
        ),
    ]
