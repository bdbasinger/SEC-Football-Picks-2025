# Generated by Django 4.2.18 on 2025-01-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="week",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
