# Generated by Django 5.0.7 on 2024-10-21 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_beforestartjob_options_alter_process_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order_service', 'created_at'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RenameField(
            model_name='service',
            old_name='order',
            new_name='order_service',
        ),
    ]
