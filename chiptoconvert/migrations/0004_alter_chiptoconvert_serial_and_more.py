# Generated by Django 4.1 on 2022-08-22 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chiptoconvert', '0003_remove_chiptoconvert_x_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiptoconvert',
            name='serial',
            field=models.CharField(default='--', max_length=50),
        ),
        migrations.AlterField(
            model_name='chiptoconvert',
            name='vlrcobrado',
            field=models.CharField(default='--', max_length=10),
        ),
        migrations.AlterField(
            model_name='chiptoconvert',
            name='x',
            field=models.CharField(default='--', max_length=200),
        ),
    ]