# Generated by Django 4.0.2 on 2022-06-07 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0145_remove_faction_posterwar'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='warAgainst',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='FactionTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_id', models.IntegerField(default=0)),
                ('name', models.CharField(default='target_name', max_length=16)),
                ('rank', models.CharField(default='rank', max_length=128)),
                ('level', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('update_timestamp', models.IntegerField(default=0)),
                ('life_current', models.IntegerField(default=0)),
                ('life_maximum', models.IntegerField(default=1)),
                ('last_action_timestamp', models.IntegerField(default=0)),
                ('last_action_relative', models.CharField(blank=True, default='last_action_relative', max_length=32, null=True)),
                ('last_action_status', models.CharField(default='Offline', max_length=16)),
                ('status_description', models.CharField(blank=True, default='status_description', max_length=64, null=True)),
                ('status_details', models.CharField(blank=True, default='status_details', max_length=128, null=True)),
                ('status_state', models.CharField(blank=True, default='status_state', max_length=32, null=True)),
                ('status_color', models.CharField(blank=True, default='green', max_length=16, null=True)),
                ('status_until', models.IntegerField(default=0)),
                ('faction_position', models.CharField(default='faction_position', max_length=32)),
                ('faction_name', models.CharField(default='faction_name', max_length=64)),
                ('faction_faction_id', models.IntegerField(default=0)),
                ('faction_faction_dif', models.IntegerField(default=0)),
                ('strength', models.BigIntegerField(default=0)),
                ('speed', models.BigIntegerField(default=0)),
                ('defense', models.BigIntegerField(default=0)),
                ('dexterity', models.BigIntegerField(default=0)),
                ('total', models.BigIntegerField(default=0)),
                ('strength_timestamp', models.IntegerField(default=0)),
                ('speed_timestamp', models.IntegerField(default=0)),
                ('defense_timestamp', models.IntegerField(default=0)),
                ('dexterity_timestamp', models.IntegerField(default=0)),
                ('total_timestamp', models.IntegerField(default=0)),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faction.faction')),
            ],
        ),
    ]
