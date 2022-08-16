# Generated by Django 4.0.2 on 2022-08-16 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0021_board_boardfile_alter_board_credate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='boardfile',
            field=models.FileField(blank=True, default=None, upload_to='boardpic/'),
        ),
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 18, 34, 42, 753114)),
        ),
        migrations.AlterField(
            model_name='board',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='low/boardpic/'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 18, 34, 42, 753114)),
        ),
    ]
