from django.contrib import admin
from .models import Post, PostList


#admin.site.register(Contact)
#admin.site.register(Post)


class PostListAdmin(admin.StackedInline):
    model = PostList

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostListAdmin]

    class Meta:
       model = Post

@admin.register(PostList)
class PostListAdmin(admin.ModelAdmin):
    pass