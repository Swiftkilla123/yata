# Generated by Django 3.1.2 on 2020-11-29 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0021_auto_20201129_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='companystock',
            name='delta_positions',
            field=models.TextField(default='{}'),
        ),
    ]