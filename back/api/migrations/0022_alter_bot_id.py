# Generated by Django 4.2.1 on 2023-05-20 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_bot_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
