# Generated by Django 2.1.2 on 2019-01-02 08:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190102_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 8, 17, 48, 787243, tzinfo=utc)),
        ),
    ]
