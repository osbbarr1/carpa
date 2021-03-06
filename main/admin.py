from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'update_date')
    fieldsets = (
        ('Audit', {
            'fields': ('creation_date', 'update_date'),
        })
    )
