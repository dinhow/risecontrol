# Generated by Django 4.1 on 2022-08-31 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chip', '0005_alter_chip_amount_charged_alter_chip_amount_nf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='chip_apn',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='chip',
            name='chip_company',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]