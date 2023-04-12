# Generated by Django 4.1.7 on 2023-04-10 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sportevent", "0009_alter_resultevent_athlete"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="registration_end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 10, 21, 39, 38, 689956),
                help_text="Enter the end date of registration for the event",
                verbose_name="Registration end date",
            ),
        ),
    ]
