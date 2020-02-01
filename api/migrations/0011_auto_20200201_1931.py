# Generated by Django 3.0.2 on 2020-02-01 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200201_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 16, 31, 41, 745235, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='in_school',
            field=models.CharField(default=False, max_length=10),
        ),
    ]
