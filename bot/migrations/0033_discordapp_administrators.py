# Generated by Django 3.0.1 on 2020-02-20 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0032_auto_20200220_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordapp',
            name='administrators',
            field=models.TextField(default='{}'),
        ),
    ]