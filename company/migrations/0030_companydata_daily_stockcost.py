# Generated by Django 4.0.5 on 2023-12-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0029_rename_effectiveness_book_bonus_company_effectiveness_book_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="companydata",
            name="daily_stockcost",
            field=models.BigIntegerField(default=0),
        ),
    ]
