from django.contrib import admin

from .models import Issue

admin.site.register(Issue)

from .models import Comment

admin.site.register(Comment)