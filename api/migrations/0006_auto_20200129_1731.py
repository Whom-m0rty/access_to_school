# Generated by Django 3.0.2 on 2020-01-29 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200129_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 17, 31, 19, 441615)),
        ),
    ]
