# Generated by Django 4.0.6 on 2022-08-02 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwm', '0006_alter_user_credate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.TextField(blank=True, default='<django.db.models.fields.CharField>comment'),
        ),
        migrations.AlterField(
            model_name='user',
            name='credate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 3, 1, 5, 19, 649351)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, default='def@def', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='usrprophoto/<built-in function id>'),
        ),
    ]