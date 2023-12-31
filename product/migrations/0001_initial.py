# Generated by Django 4.2.3 on 2023-07-12 06:56

from django.db import migrations, models
import product.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(
                        help_text="format: required, max-200",
                        max_length=200,
                        verbose_name="product name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        help_text="format: required, letters, numbers etc",
                        max_length=200,
                        verbose_name="Product SAFE URL",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="format: required", verbose_name="product description"
                    ),
                ),
                (
                    "sale_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_lenght": "the price must be between 0 and 99999999.99"
                            }
                        },
                        help_text="format: maximum price 99999999.99",
                        max_digits=10,
                        verbose_name="sale price",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="product_images/no-food.webp",
                        help_text="format: not required",
                        null=True,
                        upload_to=product.utils.get_upload_path,
                        verbose_name="product image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        help_text="format: not required",
                        max_length=200,
                        null=True,
                        verbose_name="Alternative text for image",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="format: true=product visible",
                        verbose_name="product visibility",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date product created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="format: Y-m-d H:M:S",
                        verbose_name="date product last updated",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
