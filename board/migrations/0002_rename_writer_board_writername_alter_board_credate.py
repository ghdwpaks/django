# Generated by Django 4.0.6 on 2022-08-05 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='writer',
            new_name='writername',
        ),
        migrations.AlterField(
            model_name='board',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 10, 45, 1, 519779)),
        ),
    ]
