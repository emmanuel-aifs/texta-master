# Generated by Django 2.2.28 on 2022-05-12 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0010_labelset_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelset',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Project'),
        ),
    ]
