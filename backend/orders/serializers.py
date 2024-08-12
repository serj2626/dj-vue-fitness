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

    class Meta:
        model = OrderTraining
        fields = "__all__"

class OrderTrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderTraining
        fields = (
            "rate",
            "start",
        )
