from django.contrib import admin as django_admin

from base.admin import BaseAdmin
from .models import Section as SectionModel
from .models import Process as ProcessModel
from .models import BeforeStartJob as BeforeStartJobModel
from .models import TeamMember as TeamMemberModel
from .models import Tab as TabModel
from .models import Service as ServiceModel


class SectionAdmin(BaseAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


class ProcessAdmin(BaseAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)


class BeforeStartJobAdmin(BaseAdmin):
    list_display = ('title', 'description')
    search_fields = list_display


class TeamMemberAdmin(django_admin.ModelAdmin):
    list_display = ('position',)
    search_fields = ('position',)


class TabAdmin(django_admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    filter_horizontal = ('sections', 'processes', 'before_start_job', 'team')


class ServiceAdmin(django_admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    filter_horizontal = ('tabs',)


# Registering models in admin
django_admin.site.register(SectionModel, SectionAdmin)
django_admin.site.register(ProcessModel, ProcessAdmin)
django_admin.site.register(BeforeStartJobModel, BeforeStartJobAdmin)
django_admin.site.register(TeamMemberModel, TeamMemberAdmin)
django_admin.site.register(TabModel, TabAdmin)
django_admin.site.register(ServiceModel, ServiceAdmin)
