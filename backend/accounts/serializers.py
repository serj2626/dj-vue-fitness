from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):

        user_exist = User.objects.filter(email=validated_data['email']).exists()
        if user_exist:
            raise serializers.ValidationError('Пользователь с таким email уже существует')

        psw = validated_data.pop('password')
        if len(psw) < 8:
            raise serializers.ValidationError('Пароль должен быть не менее 8 символов')
        
        user = User.objects.create_user(**validated_data)
        user.set_password(psw)
        user.save()
        return user
