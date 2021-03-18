# Generated by Django 3.1.7 on 2021-03-18 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20210318_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='technique',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='artwork',
            name='year_completed',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
