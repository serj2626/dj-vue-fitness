from rest_framework import serializers
from .models import Trainer, RatingTrainer, Reviews, Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source='get_position_display')
    class Meta:
        model = Trainer
        fields = '__all__'
