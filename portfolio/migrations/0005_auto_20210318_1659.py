# Generated by Django 3.1.7 on 2021-03-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210318_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=256),
        ),
    ]
