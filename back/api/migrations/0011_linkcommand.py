# Generated by Django 4.2.1 on 2023-05-15 09:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_botchat'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkCommand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('current', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current', to='api.command')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='api.command')),
            ],
        ),
    ]
