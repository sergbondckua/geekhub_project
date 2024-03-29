# Generated by Django 4.1.7 on 2023-03-04 15:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Athlete",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата народження"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "Чоловіча"), ("female", "Жіноча")],
                        max_length=10,
                        verbose_name="Стать",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="Номер телефону"
                    ),
                ),
                (
                    "emergency_contact_name",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        verbose_name="Ім'я екстреного контакту",
                    ),
                ),
                (
                    "emergency_contact_phone",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        verbose_name="Номер телефону екстреного контакту",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Населений пункт"
                    ),
                ),
                (
                    "club",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Спортивний клуб"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Атлета",
                "verbose_name_plural": "Атлети",
                "ordering": ("username",),
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                    models.DateTimeField(auto_now_add=True, verbose_name="Створено"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Оновлено"),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Назва")),
                ("date_event", models.DateField(verbose_name="Дата проведення")),
                (
                    "location",
                    models.CharField(max_length=200, verbose_name="Місце проведення"),
                ),
                ("description", models.TextField(blank=True, verbose_name="Опис")),
            ],
            options={
                "verbose_name": "Спортивний захід",
                "verbose_name_plural": "Спортивні заходи",
                "ordering": ("date_event",),
            },
        ),
        migrations.CreateModel(
            name="Distance",
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
                    models.DateTimeField(auto_now_add=True, verbose_name="Створено"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Оновлено"),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Назва")),
                (
                    "distance_in_unit",
                    models.PositiveSmallIntegerField(verbose_name="Дистанція"),
                ),
                (
                    "athlete",
                    models.ManyToManyField(
                        blank=True, related_name="athletes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="sportevent.event",
                    ),
                ),
            ],
            options={
                "verbose_name": "Дистанція",
                "verbose_name_plural": "Дистанції",
                "ordering": ("event",),
            },
        ),
    ]
