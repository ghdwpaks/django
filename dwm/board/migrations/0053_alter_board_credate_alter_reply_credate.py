# Generated by Django 4.0.2 on 2022-08-23 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0052_alter_board_credate_alter_reply_credate_likey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 24, 1, 0, 33, 224861)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 24, 1, 0, 33, 224861)),
        ),
    ]