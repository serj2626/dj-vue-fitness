from django.contrib.auth import get_user_model
from rest_framework import serializers

from workout.models import Rate, Trainer
from workout.serializers import RateSerializer, TrainerSerializer

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


class OrderTrainingListSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer()
    rate = RateSerializer()
    start = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")
    end = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S")

    class Meta:
        model = OrderTraining
        fields = "__all__"


class OrderTrainingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTraining
        fields = ("rate", "start", "trainer")
