# Generated by Django 3.1.1 on 2020-09-22 16:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_url', models.URLField(unique=True)),
                ('url_hash', models.URLField(unique=True)),
                ('clicks', models.IntegerField(default=0)),
                ('shortened_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='applications.application')),
            ],
        ),
    ]
