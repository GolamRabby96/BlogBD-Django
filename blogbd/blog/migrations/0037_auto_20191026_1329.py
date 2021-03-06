# Generated by Django 2.1.2 on 2019-10-26 07:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20191010_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 7, 29, 26, 56062, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='author',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 26, 7, 29, 26, 56062, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 26, 7, 29, 26, 71683, tzinfo=utc)),
        ),
    ]
