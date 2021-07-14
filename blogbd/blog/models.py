from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
# Create your models here.
#
# CHOICES=[('M','Male'),('F','Female')]
class Author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    home_town = models.CharField(max_length=255, blank=True)
    form_town = models.CharField(max_length=255, blank=True)
    study = models.CharField(max_length=255, blank=True)
    went_to = models.CharField(max_length=255, blank=True)
    birth_day = models.DateField(auto_now=False,auto_now_add=False)
    join_date = models.DateField(default=timezone.now())
    profile_picture = models.ImageField(upload_to="profile_pics",blank=True)
    cover_picture = models.ImageField(upload_to="cover_picture",blank=True)

    def __str__(self):
        return self.name.username


class Article(models.Model):
    article_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    post_cat = (
        ('Photography', 'Photography'),
        ('Movies', 'Movies'),
        ('Career', 'Career'),
        ('Gamming', 'Gamming'),
        ('Political', 'Political'),
        ('Nature', 'Nature'),
        ('Education', 'Education'),
        ('Business', 'Business'),
        ('Marketing', 'Marketing'),
        ('Food', 'Food'),
        ('Beauty', 'Beauty'),
    )
    post_categori = models.CharField(max_length=255, choices=post_cat)
    post_title = models.CharField(max_length=255)
    post_body = models.TextField()
    likes = models.ManyToManyField(Author,blank=True,related_name='post_like')
    post_image = models.ImageField(upload_to=settings.MEDIA_ROOT,blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publis_now(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    comment_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.comment_post.post_title

class Contact(models.Model):
    email_auth = models.ForeignKey(Author, on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email_body = models.TextField()

    def __str__(self):
        return self.username


class Groups(models.Model):
    group_name = models.CharField(max_length=80)
    group_member = models.ManyToManyField(Author, related_name='Membership')
    group_cover_picture = models.ImageField(upload_to="cover_picture",blank=True)
    super_auth = models.ForeignKey(Author, on_delete=models.CASCADE)
    group_create_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.group_name




class GroupArticle(models.Model):
    group_article_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    group_post_title = models.CharField(max_length=255)
    group_post_body = models.TextField()
    group_post_likes = models.ManyToManyField(Author,blank=True,related_name='group_post_like')
    group_post_image = models.ImageField(upload_to='group_photo',blank=True)
    group_post_create_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.group_post_title


class GroupComment(models.Model):
    group_comment_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    group_comment_post = models.ForeignKey(GroupArticle, on_delete=models.CASCADE)
    group_comment = models.TextField()
    group_comment_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.group_comment_post.group_post_title

class RequestGroup(models.Model):
    whichgroup = models.ForeignKey(Groups, on_delete=models.CASCADE)
    who = models.ForeignKey(Author, on_delete=models.CASCADE)


class Doner(models.Model):
    doner_auth=models.ForeignKey(Author, on_delete=models.CASCADE)
    div_do=(
        ('Dhaka','dhaka'),
        ('Khulna','khulna'),
        ('Barisal','Barisal'),
        ('Rajshahi','rajshahi'),
        ('Sylhet','sylhet'),
        ('Rangpur','rangpur'),
        ('Mymensingh','mymensingh'),
        ('Chittagong','chittagong'),
    )
    division = models.CharField(max_length=255, choices=div_do)
    dis_do=(
        ('','---------'),
        ('','........................DHAKA DIVISION'),
        ('Dhaka','Dhaka'),('Faridpur','Faridpur'),
        ('Gazipur','Gazipur'),('Gopalganj','Gopalganj'),
        ('Kishoreganj','Kishoreganj'),('Madaripur','Madaripur'),
        ('Manikganj','Manikganj'),('Munshiganj','Munshiganj'),
        ('Narayanganj','Narayanganj'),('Munshiganj','Munshiganj'),
        ('Narsingdi','Narsingdi'),('Rajbari','Rajbari'),
        ('Shariatpur','Shariatpur'),('Tangail','Tangail'),

        ('','........................KHUNA DIVISION'),
        ('Khulna','Khulna'),('Kushtia','Kushtia'),
        ('Bagerhat','Bagerhat'),('Chuadanga','Chuadanga'),
        ('Jessore','Jessore'),('Jhenaidah','Jhenaidah'),
        ('Magura','Magura'),('Meherpur','Meherpur'),
        ('Narail','Narail'),('Meherpur','Meherpur'),
        ('Satkhira','Satkhira'),


        ('','........................BARISAL DIVISION'),
        ('Barisal','Barisal'),('Barguna','Barguna'),
        ('Bhola','Bhola'),('Jhalokati','Jhalokati'),
        ('Patuakhali','Patuakhali'),('Pirojpur','Pirojpur'),


        ('','........................RAJSHAHI DIVISION'),
        ('Rajshahi','Rajshahi'),('Bogra','Bogra'),('Joypurhat','Joypurhat'),
        ('Naogao','Naogao'),('Natore','Natore'),
        ('Chapainawabganj','Chapainawabganj'),('Pabna','Pabna'),
        ('Sirajganj','Sirajganj'),


        ('','........................SYLHET DIVISION'),
        ('Sylhet','Sylhet'),('Habiganj','Habiganj'),('Moulvibazar','Moulvibazar'),
        ('Sunamganj','Sunamganj'),


        ('','........................RANGPUR DIVISION'),
        ('Rangpur','Rangpur'),('Dinajpur','Dinajpur'),('Gaibandha','Gaibandha'),
        ('Kurigram','Kurigram'),('Lalmonirhat','Lalmonirhat'),
        ('Nilphamari','Nilphamari'),('Panchagarh','Panchagarh'),
        ('Thakurgaon','Thakurgaon'),


        ('','........................MYMENSINGH DIVISION'),
        ('Mymensingh','Mymensingh'),('Jamalpur','Jamalpur'),
        ('Netrokona','Netrokona'),('Sherpur','Sherpur'),

        ('','........................CHITTAGONG DIVISION'),
        ('Chittagong','Chittagong'),('Bandarban','Bandarban'),('Brahmanbaria','Brahmanbaria'),
        ('Chandpur','Chandpur'),
        ('Comilla','Comilla'),("Cox's Bazar","Cox's Bazar"),
        ('Feni','Feni'),('Khagrachhari','Khagrachhari'),
        ('Lakshmipur','Lakshmipur'),('Noakhali','Noakhali'),
        ('Rangamati','Rangamati'),
    )
    district = models.CharField(max_length=255, choices=dis_do)
    bl_g=(
        ('A+','A+'),('AB+','AB+'),("AB-","AB-"),('B+',"B+"),
        ('B-','B-'),('O+','O+'),('O-','O-')
    )
    blood_group = models.CharField(max_length=255, choices=bl_g)
    number = models.IntegerField()
    def __str__(self):
        return self.doner_auth.name.username
