# Generated by Django 2.2.7 on 2019-11-23 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20191124_0411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('imdb_id',)},
        ),
    ]
