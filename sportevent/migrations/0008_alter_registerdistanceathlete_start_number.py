# Generated by Django 4.1.7 on 2023-03-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sportevent", "0007_alter_registerdistanceathlete_start_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registerdistanceathlete",
            name="start_number",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, unique=True, verbose_name="Номер учасника"
            ),
        ),
    ]
