from django.contrib import admin
from .models import Comment, ReplyComment
# Register your models here.
admin.site.register(Comment)
admin.site.register(ReplyComment)