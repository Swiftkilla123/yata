# Generated by Django 5.0.4 on 2024-04-22 19:02

import chat.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0077_player_key_last_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersistentRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('room_staff', models.BooleanField(default=False)),
                ('version', models.IntegerField(default=1)),
                ('slug', models.SlugField(max_length=35)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
        migrations.CreateModel(
            name='RoomMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('received', chat.models.CustomDateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.persistentroom')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='player.player')),
            ],
            options={
                'ordering': ['received'],
            },
        ),
        migrations.CreateModel(
            name='RoomSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ManyToManyField(to='chat.persistentroom')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
    ]
