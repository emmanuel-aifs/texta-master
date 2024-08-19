# Generated by Django 2.1.15 on 2020-04-29 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('embedding', '0010_auto_20200312_1804'),
        ('topic_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clusteringresult',
            name='embedding',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='embedding.Embedding'),
        ),
        migrations.AddField(
            model_name='clusteringresult',
            name='significant_words_filter',
            field=models.CharField(default='[0-9]+', max_length=100),
        ),
    ]
