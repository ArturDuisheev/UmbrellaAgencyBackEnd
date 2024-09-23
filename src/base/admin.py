from django.contrib import admin as django_admin


class BaseAdmin(django_admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
