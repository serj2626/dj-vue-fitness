from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request

from .models import Abonement, OrderAbonement, OrderTraining
from .serializers import (
    AbonementSerializer,
    OrderAbonementSerializer,
    OrderTrainingCreateSerializer,
)


class AbonemenListtView(ListAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer

    @extend_schema(summary="Список абонементов с тарифами")
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderAbonementCreateView(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = OrderAbonementSerializer
    queryset = OrderAbonement.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)

    @extend_schema(
        summary="Бронировать абонемент",
        description="Бронировать абонемент по id абонемента",
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderTrainingCreateView(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = OrderTrainingCreateSerializer
    queryset = OrderTraining.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)

    @extend_schema(summary="Бронировать тренировку")
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
