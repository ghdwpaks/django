# Generated by Django 4.0.2 on 2022-08-12 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwm', '0035_alter_user_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 12, 12, 56, 0, 197731)),
        ),
    ]