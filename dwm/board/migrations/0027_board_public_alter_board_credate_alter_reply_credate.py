# Generated by Django 4.0.2 on 2022-08-18 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0026_alter_board_credate_alter_reply_credate'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 22, 9, 7, 673829)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 22, 9, 7, 673829)),
        ),
    ]