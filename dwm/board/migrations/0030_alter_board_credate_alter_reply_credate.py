# Generated by Django 4.0.6 on 2022-08-19 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0029_alter_board_credate_alter_reply_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 9, 58, 48, 944152)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 9, 58, 48, 943167)),
        ),
    ]
