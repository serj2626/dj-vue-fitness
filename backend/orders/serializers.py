from rest_framework import serializers
from .models import OrderAbonement, Abonement



class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        fields = '__all__'