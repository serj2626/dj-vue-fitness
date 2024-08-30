from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from orders.models import OrderAbonement, OrderTraining
from orders.serializers import OrderAbonementListSerializer, OrderTrainingListSerializer
from rest_framework.pagination import PageNumberPagination
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


class MyTrainingPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class MytrainingListView(ListAPIView):
    pagination_class = MyTrainingPagination
    serializer_class = OrderTrainingListSerializer

    def get_queryset(self):
        return OrderTraining.objects.filter(user=self.request.user)

    @extend_schema(summary="Список моих тренировок")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MytrainingDeleteView(DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = OrderTrainingListSerializer
    queryset = OrderTraining.objects.all()

    @extend_schema(summary="Удалить тренировку")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @extend_schema(summary="Изменить тренировку")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class MyAbonementListView(ListAPIView):

    serializer_class = OrderAbonementListSerializer

    def get_queryset(self):
        return OrderAbonement.objects.filter(user=self.request.user)

    @extend_schema(summary="Список моих абонементов")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MyAbonementDeleteView(DestroyModelMixin, GenericAPIView):
    serializer_class = OrderAbonementListSerializer
    queryset = OrderAbonement.objects.all()

    @extend_schema(summary="Удалить абонемент")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@extend_schema(summary="Регистрация")
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
