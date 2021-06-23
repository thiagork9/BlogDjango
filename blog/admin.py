from django.contrib import admin

from.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("tittle", "slug", "created", "update", "author")#campos que irão aparecer
    prepopulated_fields = {"slug": ("tittle",)}#preenchimento do slug com o titulo

