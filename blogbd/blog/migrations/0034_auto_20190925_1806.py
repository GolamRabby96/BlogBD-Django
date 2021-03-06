# Generated by Django 2.1.2 on 2019-09-25 12:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20190908_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 25, 12, 6, 23, 346374, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='post_categori',
            field=models.CharField(choices=[('Photograpy', 'Photograpy'), ('Movies', 'Movies'), ('Career', 'Career'), ('Gamming', 'Gamming'), ('Political', 'Political'), ('Nature', 'Nature'), ('Education', 'Education'), ('Business', 'Business'), ('Marketting', 'Marketting'), ('Food', 'Food'), ('Beauty', 'Beauty')], max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 25, 12, 6, 23, 346374, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 25, 12, 6, 23, 361995, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doner',
            name='district',
            field=models.CharField(choices=[('', '---------'), ('', '........................DHAKA DIVISION'), ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Narayanganj', 'Narayanganj'), ('Munshiganj', 'Munshiganj'), ('Narsingdi', 'Narsingdi'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Tangail', 'Tangail'), ('', '........................KHUNA DIVISION'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jessore', 'Jessore'), ('Jhenaidah', 'Jhenaidah'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Meherpur', 'Meherpur'), ('Satkhira', 'Satkhira'), ('', '........................BARISAL DIVISION'), ('Barisal', 'Barisal'), ('Barguna', 'Barguna'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('', '........................RAJSHAHI DIVISION'), ('Rajshahi', 'Rajshahi'), ('Bogra', 'Bogra'), ('Joypurhat', 'Joypurhat'), ('Naogao', 'Naogao'), ('Natore', 'Natore'), ('Chapainawabganj', 'Chapainawabganj'), ('Pabna', 'Pabna'), ('Sirajganj', 'Sirajganj'), ('', '........................SYLHET DIVISION'), ('Sylhet', 'Sylhet'), ('Habiganj', 'Habiganj'), ('Moulvibazar', 'Moulvibazar'), ('Sunamganj', 'Sunamganj'), ('', '........................RANGPUR DIVISION'), ('Rangpur', 'Rangpur'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Thakurgaon', 'Thakurgaon'), ('', '........................MYMENSINGH DIVISION'), ('Mymensingh', 'Mymensingh'), ('Jamalpur', 'Jamalpur'), ('Netrokona', 'Netrokona'), ('Sherpur', 'Sherpur'), ('', '........................CHITTAGONG DIVISION'), ('Chittagong', 'Chittagong'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Comilla', 'Comilla'), ("Cox's Bazar", "Cox's Bazar"), ('Feni', 'Feni'), ('Khagrachhari', 'Khagrachhari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati')], max_length=255),
        ),
        migrations.AlterField(
            model_name='doner',
            name='division',
            field=models.CharField(choices=[('Dhaka', 'dhaka'), ('Khulna', 'khulna'), ('Barisal', 'Barisal'), ('Rajshahi', 'rajshahi'), ('Sylhet', 'sylhet'), ('Rangpur', 'rangpur'), ('Mymensingh', 'mymensingh'), ('Chittagong', 'chittagong')], max_length=255),
        ),
    ]
