from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Abonement, OrderAbonement, OrderTraining


User = get_user_model()


class OrderAbonementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAbonement
        fields = "__all__"


class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        fields = "__all__"



class OrderAbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAbonement
        fields = (
            "abonement",
            "start",
        )


class OrderTrainingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    trainer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OrderTraining
        fields = ("rate", "start", "user", "trainer")
