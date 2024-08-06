from rest_framework import serializers
from .models import OrderAbonement, Abonement, OrderTraining


class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        fields = '__all__'


class OrderAbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAbonement
        fields = ('phone', 'abonement', 'start',)


class OrderTrainingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    trainer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = OrderTraining
        fields = ('rate', 'start',  'user', 'trainer')
