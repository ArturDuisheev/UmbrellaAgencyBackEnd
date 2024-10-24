# Generated by Django 5.0.7 on 2024-10-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_section_options_remove_process_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beforestartjob',
            options={'ordering': ['order', 'created_at'], 'verbose_name': 'До начала работы', 'verbose_name_plural': 'До начала работ'},
        ),
        migrations.AlterModelOptions(
            name='process',
            options={'ordering': ['order', 'created_at'], 'verbose_name': 'Процесс', 'verbose_name_plural': 'Процессы'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['order', 'created_at'], 'verbose_name': 'Секция', 'verbose_name_plural': 'Секции'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order', 'created_at'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='tab',
            options={'ordering': ['order', 'created_at'], 'verbose_name': 'Таб', 'verbose_name_plural': 'Табы'},
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ['order', 'created_at'], 'verbose_name': 'Член команды', 'verbose_name_plural': 'Члены команды'},
        ),
        migrations.AddField(
            model_name='beforestartjob',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Позиция для сортировки', verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='process',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Позиция для сортировки', verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Позиция для сортировки', verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Позиция для сортировки', verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='tab',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Позиция для сортировки', verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Позиция для сортировки', verbose_name='Порядок'),
        ),
    ]
