# Generated by Django 2.2.28 on 2022-05-12 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_task_task_type'),
        ('annotator', '0009_annotator_annotator_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelset',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Project'),
        ),
    ]
