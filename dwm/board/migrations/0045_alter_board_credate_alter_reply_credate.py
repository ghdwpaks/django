# Generated by Django 4.0.2 on 2022-08-19 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0044_alter_board_credate_alter_reply_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 1, 3, 21, 250600)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 1, 3, 21, 249570)),
        ),
    ]