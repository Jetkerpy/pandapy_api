import re
from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import get_upload_path
# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_("product name"),
        help_text=_("format: required, max-200")
    )
    slug = models.SlugField(
        max_length=200,
        verbose_name=_("Product SAFE URL"),
        help_text=_("format: required, letters, numbers etc"),
        blank=True
    )
    description = models.TextField(
        verbose_name=_("product description"),
        help_text=_("format: required")
    )
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        unique=False,
        verbose_name=_("sale price"),
        help_text=_("format: maximum price 99999999.99"),
        error_messages={
            "name":{
                "max_lenght": _("the price must be between 0 and 99999999.99")
            }
        }
    )
    image = models.ImageField(
        _("product image"),
        upload_to = get_upload_path,
        help_text=_("format: not required"),
        blank = True,
        null = True,
        default = "product_images/no-food.webp"
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text for image"),
        blank=True,
        null=True,
        max_length=200,
        help_text=_("format: not required"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible")
    )
    created_at = models.DateTimeField(
        auto_now_add= True,
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S")
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        verbose_name=_("date product last updated"),
        help_text=_("format: Y-m-d H:M:S")
    )


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        name = self.name.lower()
        slug_name = re.sub(r"\s", "-", name)
        self.slug = slug_name
        self.alt_text = slug_name
        super().save(*args, **kwargs)