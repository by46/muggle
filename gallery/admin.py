from django.contrib import admin

from .models import Photo, Item


# Register your models here.

class PhotoInline(admin.StackedInline):
    model = Photo


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
