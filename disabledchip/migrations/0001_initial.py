# Generated by Django 4.1 on 2022-08-18 21:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('chip_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('chip_iccid', models.CharField(default='', max_length=22, unique=True)),
                ('chip_company', models.CharField(default='', max_length=20)),
                ('chip_apn', models.CharField(default='', max_length=20)),
                ('chip_status', models.IntegerField(default=1)),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('linked_at', models.DateTimeField(auto_now=True)),
                ('linked_by', models.CharField(default='', max_length=50)),
                ('linked_in', models.CharField(default='', max_length=50, unique=True)),
                ('cancelled_by', models.CharField(default='', max_length=50)),
                ('cancelled_at', models.DateTimeField(auto_now=True)),
                ('chip_with', models.CharField(default='', max_length=50)),
                ('chip_with_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
