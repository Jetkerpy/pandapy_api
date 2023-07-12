import random
import string

from .models import UserBase
from django.utils import timezone


def generate_token():
    """
        This method is generate token 6 different of digits return it
        and return also expires time this of token
    """
    token = ''.join(random.choices(string.digits, k=6))
    expires_at = timezone.now() + timezone.timedelta(minutes=3)
    return token, expires_at



def verify_token(token, phon_number):
    """
        This method take token and phone number, 
        if token and expires_at is cool :) 
        return True other way False
    """
    try:
        account = UserBase.objects.filter(phone_number = phon_number).last()
        if account and account.phone_token == token and account.expires_at > timezone.now():
            account.is_active = True
            account.save()
            return account
        return False
    except UserBase.DoesNotExist:
        return False