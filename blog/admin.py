from django.contrib import admin

from .models import Post


class ListandoPost(admin.ModelAdmin):
    list_display=('id', 'titulo', 'data')
    search_fields = ('titulo',)
    list_display_links=('id', 'titulo')


admin.site.register(Post, ListandoPost)