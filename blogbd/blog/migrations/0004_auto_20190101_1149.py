# Generated by Django 2.1.2 on 2019-01-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181231_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='gender',
        ),
        migrations.AlterField(
            model_name='article',
            name='post_categori',
            field=models.CharField(choices=[('Photograpy', 'Photograpy'), ('muvie', 'muvie'), ('Carrer', 'Carrer'), ('Gamming', 'Gamming'), ('Political', 'Political'), ('Nature', 'Nature'), ('Education', 'Education'), ('Business', 'Business'), ('Marketting', 'Marketting'), ('Food', 'Food'), ('Beuity', 'Beuity')], max_length=255),
        ),
    ]
