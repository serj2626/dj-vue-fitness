from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from workout.models import Trainer
from rest_framework.response import Response


from .models import Abonement, OrderAbonement, OrderTraining
from .serializers import (
    AbonementSerializer,
    OrderAbonementSerializer,
    OrderTrainingSerializer,
)


class AbonemenListtView(ListAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer


class OrderAbonementCreateView(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = OrderAbonementSerializer
    queryset = OrderAbonement.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderTrainingCreateView(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = OrderTrainingSerializer
    queryset = OrderTraining.objects.all()

    def perform_create(self, serializer):
        trainer = Trainer.objects.get(id=self.kwargs["pk"])
        user = self.request.user
        serializer.save(user=user, trainer=trainer)
        return super().perform_create(serializer)
