# Generated by Django 4.0.5 on 2022-08-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0060_remove_credential_chat_delete_chat_delete_credential'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='start',
            field=models.IntegerField(default=0, help_text='Date from which the contract starts'),
        ),
    ]