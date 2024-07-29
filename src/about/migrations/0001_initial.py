# Generated by Django 5.0.7 on 2024-07-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в: ')),
                ('fullname', models.CharField(max_length=120, verbose_name='ФИО')),
                ('position', models.CharField(max_length=120, verbose_name='Должность')),
                ('quote', models.CharField(blank=True, max_length=120, null=True, verbose_name='Цитата')),
                ('image', models.ImageField(blank=True, null=True, upload_to='founders/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Основатель',
                'verbose_name_plural': 'Основатели',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в: ')),
                ('title', models.CharField(max_length=120, verbose_name='Должность')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
