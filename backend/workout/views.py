from drf_spectacular.utils import extend_schema
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Post, Rate, Reviews, Subscription, Trainer
from .serializers import (
    PostListSerializer,
    PostSerializer,
    RateSerializer,
    ReviewsSerializer,
    SubscriptionSerializer,
    TrainerSerializer,
)


@extend_schema(description="Список отзывов")
class ReviewsListView(ListCreateAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()


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


@extend_schema(description="Список тренеров")
class TrainerListView(ListAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()


@extend_schema(description="Детальная информация о тренере")
class TrainerDetailView(RetrieveAPIView):
    serializer_class = TrainerSerializer

    def get_queryset(self):
        return Trainer.objects.all().prefetch_related("trainer_reviews")