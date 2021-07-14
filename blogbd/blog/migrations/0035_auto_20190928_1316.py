# Generated by Django 2.1.2 on 2019-09-28 07:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20190925_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 7, 16, 17, 823453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='author',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 28, 7, 16, 17, 823453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 7, 16, 17, 823453, tzinfo=utc)),
        ),
    ]
