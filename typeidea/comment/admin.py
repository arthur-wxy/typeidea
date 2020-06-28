from django.contrib import admin

from .models import Comment
from typeidea.base_admin import BaseOwnerAdmin


@admin.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')

