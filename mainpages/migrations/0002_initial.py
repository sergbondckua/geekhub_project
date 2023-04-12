# Generated by Django 4.1.7 on 2023-04-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StaticPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Create"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Update"),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                (
                    "url",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="URL-name"
                    ),
                ),
                ("content", models.TextField(verbose_name="Content")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]