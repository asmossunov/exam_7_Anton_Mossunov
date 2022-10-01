from django.contrib import admin

from book.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_email', 'text', 'status', 'created_at', 'changed_at')
    list_filter = ('id', 'author_name', 'author_email', 'text', 'status', 'created_at', 'changed_at')
    search_fields = ('id', 'author_name', 'author_email', 'text', 'status', 'created_at', 'changed_at')
    fields = ('id', 'author_name', 'author_email', 'text', 'status')
    readonly_fields = ['id']


admin.site.register(Record, RecordAdmin)
