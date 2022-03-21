from django.contrib import admin

from .models import Article

# Register your models here.

class Articleadmin(admin.ModelAdmin):
    list_disaplay = ('pk', 'title', 'content',)

admin.site.register(Article, Articleadmin)