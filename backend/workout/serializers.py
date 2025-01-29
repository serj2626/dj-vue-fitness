from django.db.models import Sum
from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Post, Rate, Reviews, Subscription, Trainer, TrainerImage


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Подписка на рассылку
    """

    class Meta:
        model = Subscription
        fields = ("email",)

    def validate_email(self, value):
        if Subscription.objects.filter(email=value).exists():
            raise serializers.ValidationError("Вы уже подписаны на рассылку")
        return value


class PostListSerializer(serializers.ModelSerializer):
    """
    Список постов
    """

    class Meta:
        model = Post
        fields = (
            "id",
            "category",
        )


class PostSerializer(serializers.ModelSerializer):
    """
    Список постов
    """

    class Meta:
        model = Post
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    """
    Список тарифов
    """

    class Meta:
        model = Rate
        fields = "__all__"


class TrainerForReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ("id", "avatar", "first_name", "last_name")


class ReviewsSerializer(serializers.ModelSerializer):
    """
    Список отзывов
    """

    # rating = serializers.IntegerField(min_value=1, max_value=5)
    user = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", read_only=True)
    trainer = TrainerForReviewsSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = (
            "id",
            "user",
            "trainer",
            "created_at",
            "text",
            "rating",
            "date_age",
        )


class CreateReviewsSerializer(serializers.ModelSerializer):
    """
    Представление для создания отзывов
    """

    class Meta:
        model = Reviews
        fields = ("rating", "text", "trainer")

    def validate(self, data):
        if not self.context["request"].user.is_authenticated:
            raise serializers.ValidationError(
                "Оставлять отзыв могут только авторизованные пользователи"
            )
        return data


class TrainerListSerializer(serializers.ModelSerializer):
    """
    Список тренеров на домашней странице
    """

    class Meta:
        model = Trainer
        fields = ("id", "avatar")


class TrainerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerImage
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    """
    Детальная информация о тренере
    """

    trainer_reviews = ReviewsSerializer(many=True, read_only=True)
    position = serializers.CharField(source="get_position_display")
    count_reviews = serializers.SerializerMethodField()
    total_rating = serializers.SerializerMethodField()
    images = TrainerImageSerializer(many=True, read_only=True)

    class Meta:
        model = Trainer
        fields = (
            "id",
            "avatar",
            "first_name",
            "last_name",
            "position",
            "email",
            "phone",
            "trainer_reviews",
            "count_reviews",
            "total_rating",
            "images",
        )

    def get_count_reviews(self, obj):
        return obj.trainer_reviews.count()

    def get_total_rating(self, obj):
        total_sum = obj.trainer_reviews.aggregate(Sum("rating"))["rating__sum"]
        return total_sum / obj.trainer_reviews.count() if total_sum else 0
