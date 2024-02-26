# Generated by Django 4.2.5 on 2024-02-24 16:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0035_alter_ticket_ticket_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_key',
            field=models.UUIDField(default=uuid.UUID('c127984c-e21a-46b0-9b84-88e8a5d80738')),
        ),
        migrations.AlterField(
            model_name='ticket_issues',
            name='error_key',
            field=models.UUIDField(default=uuid.UUID('b5f5758f-cf58-493c-a090-26b7af3041af')),
        ),
        migrations.AlterField(
            model_name='ticket_payment',
            name='payment_id',
            field=models.UUIDField(default=uuid.UUID('2df32c53-c7bf-4832-8ea1-dec51215172d')),
        ),
    ]
