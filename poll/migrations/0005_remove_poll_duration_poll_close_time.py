# Generated by Django 4.2.5 on 2024-02-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_rename_option_polloption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='duration',
        ),
        migrations.AddField(
            model_name='poll',
            name='close_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Close Time'),
        ),
    ]
