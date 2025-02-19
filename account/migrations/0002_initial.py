# Generated by Django 4.2 on 2024-03-07 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercoverimage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile', verbose_name='Profile'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile', verbose_name='Profile'),
        ),
    ]
