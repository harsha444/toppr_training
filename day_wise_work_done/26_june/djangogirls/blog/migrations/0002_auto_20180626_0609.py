# Generated by Django 2.0.2 on 2018-06-26 06:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 26, 6, 9, 27, 562510, tzinfo=utc)),
        ),
    ]
