# Generated by Django 5.0.1 on 2024-02-03 08:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0006_jobcard_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('job_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.jobcard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpareParts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('job_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.jobcard')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
