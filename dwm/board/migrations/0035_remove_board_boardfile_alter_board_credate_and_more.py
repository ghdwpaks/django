# Generated by Django 4.0.6 on 2022-08-19 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0034_files_alter_board_credate_alter_reply_credate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='boardfile',
        ),
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 12, 54, 31, 796951)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 12, 54, 31, 795954)),
        ),
    ]