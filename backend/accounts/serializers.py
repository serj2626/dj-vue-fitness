from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError('Пользователь с таким email уже существует')

        return super().validate(attrs)

    def create(self, validated_data):

        psw = validated_data.pop('password')
        if len(psw) < 8:
            raise serializers.ValidationError(
                'Пароль должен быть не менее 8 символов')

        user = User.objects.create_user(**validated_data)
        user.set_password(psw)
        user.save()
        return user
