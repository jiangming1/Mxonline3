# Generated by Django 2.0.2 on 2018-08-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_alikey_aliyun_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='alikey',
            name='init_script',
            field=models.CharField(default='', max_length=8000, verbose_name='vswitch'),
            preserve_default=False,
        ),
    ]
