# Generated by Django 2.0.5 on 2019-10-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='npc',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]