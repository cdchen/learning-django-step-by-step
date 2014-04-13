from django.contrib import admin
from postapp.models import Post


class PostModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostModelAdmin)
