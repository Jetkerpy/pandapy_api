# Generated by Django 4.2.3 on 2023-07-12 06:56

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserBase",
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
                    "user_name",
                    models.CharField(max_length=255, verbose_name="username"),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=13,
                        unique=True,
                        validators=[account.validators.validate_uzb_phone_number],
                        verbose_name="phone_number",
                    ),
                ),
                ("phone_token", models.CharField(blank=True, max_length=6, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CUSTOMER", "Customer"),
                            ("ADMINISTRATOR", "Administrator"),
                        ],
                        default="CUSTOMER",
                        max_length=15,
                        verbose_name="status",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        default="avatars/no_photo.png",
                        upload_to="avatars",
                        verbose_name="avatar",
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date user created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date user last updated",
                    ),
                ),
                (
                    "expires_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="expiry time of token"
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
                "verbose_name": "Accounts",
                "verbose_name_plural": "Accounts",
            },
        ),
    ]
