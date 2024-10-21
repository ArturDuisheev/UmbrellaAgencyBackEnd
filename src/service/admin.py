from django.contrib import admin as django_admin

from base.admin import BaseAdmin
from .models import Section as SectionModel
from .models import Process as ProcessModel
from .models import BeforeStartJob as BeforeStartJobModel
from .models import TeamMember as TeamMemberModel
from .models import Tab as TabModel
from .models import Service as ServiceModel


class SectionAdmin(BaseAdmin):
    list_display = ('title', 'order', 'description')  # Добавляем поле order для отображения
    search_fields = ('title', 'description')
    ordering = ['order']  # Сортировка по order в админке


class ProcessAdmin(BaseAdmin):
    list_display = ('title', 'order', 'description')
    search_fields = ('title', 'description')
    ordering = ['order']


class BeforeStartJobAdmin(BaseAdmin):
    list_display = ('title', 'order', 'description')
    search_fields = ('title', 'description')
    ordering = ['order']


class TeamMemberAdmin(django_admin.ModelAdmin):
    list_display = ('position', 'order')
    search_fields = ('position',)
    ordering = ['order']


class TabAdmin(django_admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    ordering = ['order']
    filter_horizontal = ('sections', 'processes', 'before_start_job', 'team')


class ServiceAdmin(django_admin.ModelAdmin):
    list_display = ('title', 'order_service')
    search_fields = ('title',)
    ordering = ['order_service']
    filter_horizontal = ('tabs',)


# Registering models in admin
django_admin.site.register(SectionModel, SectionAdmin)
django_admin.site.register(ProcessModel, ProcessAdmin)
django_admin.site.register(BeforeStartJobModel, BeforeStartJobAdmin)
django_admin.site.register(TeamMemberModel, TeamMemberAdmin)
django_admin.site.register(TabModel, TabAdmin)
django_admin.site.register(ServiceModel, ServiceAdmin)
