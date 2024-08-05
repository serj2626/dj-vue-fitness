from rest_framework import serializers
from .models import Trainer, Reviews, Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source='get_position_display')
    class Meta:
        model = Trainer
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'