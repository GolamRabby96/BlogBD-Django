# Generated by Django 2.1.2 on 2019-01-03 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190103_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 3, 10, 46, 21, 200282, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to='blog.Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 3, 10, 46, 21, 201280, tzinfo=utc)),
        ),
    ]
