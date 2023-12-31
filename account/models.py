from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _


from .validators import validate_uzb_phone_number

# Create your models here.

class CustomUserBaseManager(BaseUserManager):
    def create_superuser(self, phone_number, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('status', 'ADMINISTRATOR')


        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )

        return self.create_user(phone_number, password, **other_fields)


    
    def create_user(self, phone_number, password, **other_fields):
        if not phone_number:
            raise ValueError(_('You must provide a phone number.'))
        
        user = self.model(phone_number = phone_number, **other_fields)

        user.set_password(password)
        user.save()
        return user



class UserBase(AbstractBaseUser, PermissionsMixin):
    """
        UserBase table for customers & admins
    """
    STATUS_OF_USER = (
        ('CUSTOMER', 'Customer'),
        ('ADMINISTRATOR', 'Administrator'),
    )

    user_name = models.CharField(_("username"), max_length=255)
    phone_number = models.CharField(_("phone_number"), max_length=13, unique=True, validators=[validate_uzb_phone_number])
    phone_token = models.CharField(max_length=6, null=True, blank=True)
    status = models.CharField(_("status"), max_length=15, choices=STATUS_OF_USER, default='CUSTOMER')
    avatar = models.ImageField(
        _("avatar"),
        upload_to = 'avatars',
        default = 'avatars/99242731.png'
    )

    #User status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add= True,
        editable=False,
        verbose_name=_("date user created"),
        help_text=_("format: Y-m-d H:M:S")
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        editable=False,
        verbose_name=_("date user last updated"),
        help_text=_("format: Y-m-d H:M:S")
    )
    expires_at = models.DateTimeField(
        _("expiry time of token"),
        null=True, 
        blank=True
    )

    objects = CustomUserBaseManager()
    
    USERNAME_FIELD = 'phone_number'


    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'
    

    def __str__(self):
        return f"{self.phone_number} & id is {self.pk}"
        