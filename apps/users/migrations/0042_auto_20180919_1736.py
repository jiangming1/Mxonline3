# Generated by Django 2.0.2 on 2018-09-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_aliboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliboard',
            name='hainan',
            field=models.CharField(max_length=200, verbose_name='海南'),
        ),
        migrations.AlterField(
            model_name='aliboard',
            name='tianjin',
            field=models.CharField(max_length=200, verbose_name='天津'),
        ),
        migrations.AlterField(
            model_name='aliboard',
            name='zhejiang',
            field=models.CharField(max_length=200, verbose_name='浙江'),
        ),
    ]
