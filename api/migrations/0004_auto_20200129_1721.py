# Generated by Django 3.0.2 on 2020-01-29 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200129_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='E3JVnvlShCUXr7TtnIbF', max_length=20, unique=True),
        ),
    ]
