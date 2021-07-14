from django.contrib import admin
from .models import Author,Article,Comment, Contact, Groups, GroupArticle, GroupComment, RequestGroup, Doner
# Register your models here.

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Groups)
admin.site.register(GroupArticle)
admin.site.register(GroupComment)
admin.site.register(RequestGroup)
admin.site.register(Doner)
