# Generated by Django 5.0.7 on 2024-09-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_service_short_description_for_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab',
            name='processes',
            field=models.ManyToManyField(blank=True, null=True, related_name='tab_processes', to='service.process', verbose_name='Процессы'),
        ),
    ]
