# Generated by Django 4.1 on 2022-08-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disabledchip', '0003_remove_disabledchip_linked_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disabledchip',
            name='add_by',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='disabledchip',
            name='cod_cliente',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
