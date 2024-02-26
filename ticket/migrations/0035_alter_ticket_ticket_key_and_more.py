# Generated by Django 4.2.5 on 2024-02-24 16:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0034_alter_ticket_ticket_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_key',
            field=models.UUIDField(default=uuid.UUID('16c164f2-a880-4841-bdaa-94761f80e9ec')),
        ),
        migrations.AlterField(
            model_name='ticket_issues',
            name='error_key',
            field=models.UUIDField(default=uuid.UUID('936c200d-0eee-4d38-9db2-e9e51a927db6')),
        ),
        migrations.AlterField(
            model_name='ticket_payment',
            name='payment_id',
            field=models.UUIDField(default=uuid.UUID('11e6d13d-c8cb-4d77-a4a4-7d2faf195a93')),
        ),
    ]
