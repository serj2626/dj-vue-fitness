from drf_spectacular.utils import extend_schema
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.response import Response


from .models import Post, Rate, RatingStar, Reviews, Subscription, Trainer
from .serializers import (
    PostListSerializer,
    PostSerializer,
    RateSerializer,
    ReviewsSerializer,
    SubscriptionSerializer,
    TrainerListSerializer,
    TrainerSerializer,
    CreateReviewsSerializer
)

class CreateReviewsView(CreateAPIView):
    serializer_class = CreateReviewsSerializer
    queryset = Reviews.objects.all()

    def perform_create(self, serializer):
        data = self.request.data
        rating = RatingStar.objects.get(value=int(data.get("rating")))
        trainer = Trainer.objects.get(id=data.get("trainer"))

        serializer.save(user=self.request.user, rating=rating, trainer=trainer)
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


@extend_schema(summary="Подписка на рассылку")
class SubscriptionView(CreateAPIView):
    """
    Подписка на рассылку
    """

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


@extend_schema(summary="Список постов")
class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


@extend_schema(summary="Детальная информация о посте")
class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    lookup_field = "category"


@extend_schema(summary="Список тарифов")
class RateListView(ListAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()


@extend_schema(summary="Список тренеров на домашней странице")
class TrainerListView(ListAPIView):
    serializer_class = TrainerListSerializer
    queryset = Trainer.objects.all()


@extend_schema(summary="Детальная информация о тренере")
class TrainerDetailView(RetrieveAPIView):
    serializer_class = TrainerSerializer

    def get_queryset(self):
        return Trainer.objects.all().prefetch_related("trainer_reviews")


@extend_schema(summary="Список тренеров на отдельной странице")
class TrainerListForPageView(ListAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
