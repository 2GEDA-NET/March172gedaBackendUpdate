# Generated by Django 4.2 on 2024-03-11 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge', models.CharField(blank=True, choices=[('login', 'login'), ('signup', 'signup'), ('post', 'post'), ('comment', 'comment'), ('chat', 'chat'), ('stick', 'stick'), ('likes', 'likes'), ('time', 'time'), ('commerce', 'commerce'), ('livestream', 'livestream'), ('ticket', 'ticket'), ('stereo', 'stereo')], null=True, verbose_name='Acknowledge')),
                ('point', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Point')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='account.userprofile', verbose_name='User Profile')),
            ],
        ),
    ]
