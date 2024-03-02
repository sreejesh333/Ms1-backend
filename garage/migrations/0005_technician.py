# Generated by Django 5.0.1 on 2024-01-21 18:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_jobcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('labour_charge', models.FloatField(default=0)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garage.employee')),
                ('job_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.jobcard')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]