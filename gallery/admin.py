from django.contrib import admin

from .models import Tag, VectorDrawing


class VectorDrawingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')


class TagDrawingAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(VectorDrawing, VectorDrawingAdmin)
admin.site.register(Tag, TagDrawingAdmin)
