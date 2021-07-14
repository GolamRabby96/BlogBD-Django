# Generated by Django 2.1.2 on 2019-07-14 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20190323_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 17, 43, 48, 224838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='author',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 14, 17, 43, 48, 224838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 17, 43, 48, 224838, tzinfo=utc)),
        ),
    ]