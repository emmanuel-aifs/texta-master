# Generated by Django 2.2.24 on 2021-11-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bert_tagger', '0005_auto_20210930_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='berttagger',
            name='use_gpu',
            field=models.BooleanField(default=True),
        ),
    ]
