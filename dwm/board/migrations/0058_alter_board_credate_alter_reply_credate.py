# Generated by Django 4.0.2 on 2022-09-10 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0057_alter_board_credate_alter_reply_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 1, 54, 23, 941501)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 1, 54, 23, 940503)),
        ),
    ]
