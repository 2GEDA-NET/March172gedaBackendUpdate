# Generated by Django 4.2.5 on 2024-02-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_rename_address_useraddress_alter_user_phone_number_and_more'),
        ('poll', '0010_poll_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polloption',
            name='voters',
            field=models.ManyToManyField(blank=True, related_name='voters', to='user.userprofile', verbose_name='Voters'),
        ),
    ]
