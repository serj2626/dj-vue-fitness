from drf_spectacular.utils import extend_schema
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import OrderTraining
from orders.serializers import (
    OrderTrainingCreateSerializer,
    OrderTrainingListSerializer,
)

from .models import Post, Rate, Reviews, Subscription, Trainer
from .serializers import (
    PostListSerializer,
    PostSerializer,
    RateSerializer,
    ReviewsSerializer,
    SubscriptionSerializer,
    TrainerListSerializer,
    TrainerSerializer,
)

# class CreateReviewsView(CreateAPIView):
#     serializer_class = CreateReviewsSerializer
#     queryset = Reviews.objects.all()

#     def perform_create(self, serializer):
#         user = self.request.user
#         trainer = Trainer.objects.get(id=self.kwargs["uuid"])
#         serializer.save(user=user, trainer=trainer)
#         return super().perform_create(serializer)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


@extend_schema(description="Список отзывов")
class ReviewsListView(ListCreateAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewsDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()

    @extend_schema(
        summary="Получить отзывы по id",
        description="Получить отзывы по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Изменить отзывы по id",
        description="Изменить отзывы по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить отзывы по id",
        description="Удалить отзывы по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить отзыв по id",
        description="Обновить отзыв по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


@extend_schema(description="Подписка на рассылку")
class SubscriptionView(CreateAPIView):
    """
    Подписка на рассылку
    """

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


@extend_schema(description="Список постов")
class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


@extend_schema(description="Детальная информация о посте")
class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    lookup_field = "category"


@extend_schema(description="Список тарифов")
class RateListView(ListAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()


@extend_schema(description="Список тренеров на домашней странице")
class TrainerListView(ListAPIView):
    serializer_class = TrainerListSerializer
    queryset = Trainer.objects.all()


@extend_schema(description="Детальная информация о тренере")
class TrainerDetailView(RetrieveAPIView):
    serializer_class = TrainerSerializer

    def get_queryset(self):
        return Trainer.objects.all().prefetch_related("trainer_reviews")


@extend_schema(description="Список тренеров на отдельной страницы")
class TrainerListForPageView(ListAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
