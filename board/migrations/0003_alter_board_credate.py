# Generated by Django 4.0.6 on 2022-08-05 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_rename_writer_board_writername_alter_board_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 10, 46, 2, 112894)),
        ),
    ]
