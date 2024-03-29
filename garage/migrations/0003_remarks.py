# Generated by Django 5.0.1 on 2024-01-21 07:25

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_employee_rename_emp_img_user_user_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remarks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
