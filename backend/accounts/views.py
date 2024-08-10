from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from orders.serializers import OrderAbonementListSerializer, OrderTrainingListSerializer
from orders.models import OrderAbonement, OrderTraining
from .serializers import RegisterSerializer

User = get_user_model()


@api_view(["GET"])
def get_my_info(request):
    return Response(
        {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        }
    )


class MytrainingListView(ListAPIView):

    serializer_class = OrderTrainingListSerializer

    def get_queryset(self):
        return OrderTraining.objects.filter(user=self.request.user)


class MyAbonementListView(ListAPIView):

    serializer_class = OrderAbonementListSerializer

    def get_queryset(self):
        return OrderAbonement.objects.filter(user=self.request.user)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        refresh = RefreshToken.for_user(user)
        data["token"] = {"refresh": str(
            refresh), "access": str(refresh.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)
