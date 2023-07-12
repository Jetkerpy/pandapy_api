from rest_framework import serializers
import re
from datetime import datetime
from string import ascii_letters
from .models import UserBase
from .utils import generate_token
from .validators import validate_uzb_phone_number


# USER SIGN UP SERIALIZER
class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = ("user_name", "phone_number", "expires_at", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "expires_at": {"read_only": True}
        }


    def to_representation(self, instance):
        representation = super().to_representation(instance)   
        time_diff = instance.expires_at - instance.created_at
        minutes = int(time_diff.total_seconds() // 60)
        representation['expires_at'] = f"The token will expire in {minutes} minutes"
        return  representation
    


    def create(self, validated_data):
        user_name = validated_data.get("user_name").capitalize()
        phone_number = validated_data.get("phone_number")
        user = UserBase.objects.create(
            phone_number = phone_number, user_name = user_name
        )
        user.set_password(validated_data['password'])
        token, expires_at = generate_token()
        user.phone_token = token
        user.expires_at = expires_at
        user.save()
        return user




    def validate_user_name(self, username):
        self.__validate_username(username)
        return username



    def validate_password(self, password):
        """
            Check password
            Bul jerde password uzinlig'i 8 den to'men bolsa
            ham keminde bir san bolmasa error beredi.
        """
        password_regex = r"^(?=.*\d).{8,}$"
        if not re.match(password_regex, password):
            raise serializers.ValidationError("Kiritilgen password keminde 8 den to'men bolmawi, ja'ne sannan 1 san boliwi kerek.")
        return password



    @classmethod
    def __validate_username(self, user_name):
        if len(user_name) == 0:
            raise serializers.ValidationError("Atin'izdi kiritiwin'iz kerek.")

        letters = ascii_letters #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

        for s in user_name:
            if len(s.strip(letters)) != 0:
                raise serializers.ValidationError("Atin'izdi tek alphabet tu'rinde kiritin'.")
# END USER SIGN UP SERIALIZER            



# VERIFY TOKEN SERIALIZER
class VerifyTokenSerializer(serializers.ModelSerializer):
    number = serializers.CharField(validators = [validate_uzb_phone_number], required = True)
    class Meta:
        model = UserBase
        fields = ('number', 'phone_token')


    def validate_number(self, phone_number):
        account = UserBase.objects.filter(phone_number = phone_number).exists()
        if not account:
            raise serializers.ValidationError(f"{phone_number} doesn't exists.")
        return phone_number


    def validate_phone_token(self, token):
        self.__verify_token(token)
        return token


    @classmethod
    def __verify_token(self, token: str):
        if len(token) != 6:
            raise serializers.ValidationError("Kiritilgen mag'liwmat toliq emes!")
        
        if not token.isdigit():
            raise serializers.ValidationError("Kiritiliwi kerek bolg'an mag'liwmat sannan ibarat boliwi kerek.")
# END VERIFY TOKEN SERIALIZER


# PROFILE SERIALIZER
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = ("id", "user_name", "phone_number", "status", "avatar", "created_at")


    def to_representation(self, instance):
        data = super().to_representation(instance)
        created_at = instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
        data['created_at'] = created_at
        return data    
# END PROFILE SERIALIZER