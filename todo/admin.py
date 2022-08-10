from django.contrib import admin
from .models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'isCompleted', 'created_at', 'update_at')
    list_filter = ('isCompleted', 'created_at', 'update_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
