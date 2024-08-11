from django.contrib.auth import get_user_model
from rest_framework import serializers

from workout.serializers import RateSerializer

from .models import Abonement, OrderAbonement, OrderTraining

User = get_user_model()


class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        fields = "__all__"


class OrderAbonementListSerializer(serializers.ModelSerializer):
    abonement = AbonementSerializer()

    class Meta:
        model = OrderAbonement
        fields = (
            "id",
            "abonement",
            "start",
            "end",
            "status",
            "active",
        )


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


class OrderTrainingListSerializer(serializers.ModelSerializer):
    trainer = serializers.StringRelatedField(read_only=True)
    rate = RateSerializer()

    class Meta:
        model = OrderTraining
        fields = (
            "id",
            "trainer",
            "rate",
            "start",
            "end",
            "status",
            "active",
        )
