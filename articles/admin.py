from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genre)
admin.site.register(Article)
admin.site.register(UserProfile)

@admin.register(Suggestions)
class PurchaseProductsAdmin(admin.ModelAdmin):
    date_heirarchy = (
        'modified',
    )
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'message'
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)