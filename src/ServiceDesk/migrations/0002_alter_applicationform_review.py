# Generated by Django 5.0.7 on 2024-10-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceDesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='review',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий или запрос клиента'),
        ),
    ]
