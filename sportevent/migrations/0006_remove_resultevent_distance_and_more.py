# Generated by Django 4.1.7 on 2023-03-25 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sportevent", "0005_alter_resultevent_athlete_alter_resultevent_distance"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resultevent",
            name="distance",
        ),
        migrations.AlterField(
            model_name="resultevent",
            name="athlete",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="results",
                to="sportevent.registerdistanceathlete",
                verbose_name="Атлет",
            ),
        ),
        migrations.AlterField(
            model_name="resultevent",
            name="result_time",
            field=models.DurationField(
                blank=True, null=True, verbose_name="Час результату"
            ),
        ),
    ]
