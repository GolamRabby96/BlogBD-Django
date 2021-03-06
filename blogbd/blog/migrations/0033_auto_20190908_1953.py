# Generated by Django 2.1.2 on 2019-09-08 13:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20190908_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 13, 53, 56, 493716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='author',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 8, 13, 53, 56, 493716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 13, 53, 56, 494715, tzinfo=utc)),
        ),
    ]
