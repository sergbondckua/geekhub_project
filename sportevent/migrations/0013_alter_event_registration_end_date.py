# Generated by Django 4.1.7 on 2023-04-11 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sportevent", "0012_alter_distance_road_map_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="registration_end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 11, 23, 57, 2, 567740),
                help_text="Enter the end date of registration for the event",
                verbose_name="Registration end date",
            ),
        ),
    ]
