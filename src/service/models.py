from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from base.models import BaseModel, BaseService


class Section(BaseService):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    description = models.TextField(
        _('Описание')
    )

    def __str__(self):
        return f'Заголовок: {self.title}, Описание секции: {self.description}'

    class Meta:
        verbose_name = _('Секция')
        verbose_name_plural = _('Секции')
        ordering = ['created_at']


class Process(BaseService):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    description = models.TextField(
        _('Описание процесса')
    )

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = _('Процесс')
        verbose_name_plural = _('Процессы')


class BeforeStartJob(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    description = models.TextField(
        _('Описание')
    )

    def __str__(self):
        return f'заголовок: {self.title}'

    class Meta:
        verbose_name = _('До начала работы')
        verbose_name_plural = _('До начала работ')


class TeamMember(BaseModel):
    position = models.CharField(
        _('Позиция'),
        max_length=120
    )

    def __str__(self):
        return f'Позиция: {self.position}'

    class Meta:
        verbose_name = _('Член команды')
        verbose_name_plural = _('Члены команды')


class Tab(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    sections = models.ManyToManyField(
        Section,
        related_name='tab_sections',
        verbose_name=_('Секции')
    )
    processes = models.ManyToManyField(
        Process,
        related_name='tab_processes',
        verbose_name=_('Процессы'),
        blank=True, null=True
    )
    before_start_job = models.ManyToManyField(
        BeforeStartJob,
        related_name='tab_before_start_job',
        verbose_name=_('До начала работы')
    )
    team = models.ManyToManyField(
        TeamMember,
        related_name='tab_team',
        verbose_name=_('Команда')
    )

    def __str__(self):
        return f'Заголовок: {self.title}'

    class Meta:
        verbose_name = _('Таб')
        verbose_name_plural = _('Табы')


class Service(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    short_description_for_banner = models.CharField(
        _('Краткое описание для баннера главной страницы'),
        help_text=_('Макс. символов: 120'),
        max_length=120,
    )
    gif = models.FileField(
        _('Гифка'),
        upload_to='gifs/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['gif',],
                message=_('Допустимые форматы: .gif')
            )
        ],
        help_text=_('Загрузите гифку для услуги. Допустимые форматы: .gif'),
    )
    tabs = models.ManyToManyField(
        Tab,
        related_name='service_tabs',
        verbose_name=_('Табы'),
    )

    def __str__(self):
        return f'Заголовок: {self.title}'

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')
