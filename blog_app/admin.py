# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog_app.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'author']


admin.site.register(Post, PostModelAdmin)
