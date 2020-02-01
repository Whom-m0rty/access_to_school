# Generated by Django 3.0.2 on 2020-02-01 16:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200201_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 16, 30, 53, 478684, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_use',
            field=models.DateTimeField(),
        ),
    ]