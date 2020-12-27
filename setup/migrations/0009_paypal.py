# Generated by Django 3.1.2 on 2020-12-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0008_analytics_last_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=32)),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
                ('signature', models.CharField(max_length=32)),
            ],
        ),
    ]