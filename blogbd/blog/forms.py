from django import forms
from .models import Author,Article,Comment,Contact, Groups, GroupArticle, GroupComment,Doner
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class RegisterDate(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['birth_day']
        widgets = {
                'birth_day': forms.DateInput(
                format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        # birth_day = forms.DateField(attr={'lavel':"hi"})
        # birth_day=forms.DateField(widget = forms.SelectDateWidget())

        # widgets = {'birth_day': forms.DateInput(format='%d/%m/%Y')}
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name','last_name','email','username','password1','password2']


class Author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields=['home_town','form_town','study','went_to','profile_picture','cover_picture']

class Article_form(forms.ModelForm):
    class Meta:
        model = Article
        fields=['post_categori','post_title','post_body','post_image']

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username','subject','email_body']
        widgets = {'email_body': forms.Textarea(attrs={'placeholder':"Please Enter Your Message"})}


class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comment']
        widgets = {'comment': forms.Textarea(attrs={'placeholder':"Enter Your comment"})}


# .....................................

class Create_group(forms.ModelForm):
    class Meta:
        model = Groups
        fields =['group_name','group_cover_picture']
        # widgets={'group_name': forms.Textarea(attrs={'placeholder':"Group Name"})}

class Group_article_form(forms.ModelForm):
    class Meta:
        model = GroupArticle
        fields=['group_post_title','group_post_body','group_post_image']

class Group_comment_form(forms.ModelForm):
    class Meta:
        model = GroupComment
        fields=['group_comment']
        widgets = {'group_comment': forms.Textarea(attrs={'placeholder':"Enter Your comment"})}

class Doner_form(forms.ModelForm):
    class Meta:
        model = Doner
        fields=['division','district','blood_group','number']
