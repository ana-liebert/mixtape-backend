# Generated by Django 4.0.3 on 2022-03-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_mix_tracklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mix',
            name='genre',
            field=models.ManyToManyField(to='api.genre'),
        ),
    ]
