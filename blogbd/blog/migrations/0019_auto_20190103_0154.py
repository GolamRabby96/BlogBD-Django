# Generated by Django 2.1.2 on 2019-01-02 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190103_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 19, 54, 12, 691396, tzinfo=utc)),
        ),
    ]
