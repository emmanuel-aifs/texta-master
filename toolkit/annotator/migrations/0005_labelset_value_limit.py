# Generated by Django 2.2.25 on 2022-01-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0004_auto_20220106_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelset',
            name='value_limit',
            field=models.IntegerField(null=True),
        ),
    ]
