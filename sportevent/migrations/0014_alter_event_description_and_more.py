# Generated by Django 4.1.7 on 2023-04-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sportevent", "0013_alter_event_registration_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Опис"),
        ),
        migrations.AlterField(
            model_name="event",
            name="registration_end_date",
            field=models.DateTimeField(
                default=None,
                help_text="Enter the end date of registration for the event",
                verbose_name="Registration end date",
            ),
        ),
    ]