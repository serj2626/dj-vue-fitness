from rest_framework import serializers

from .models import Post, Rate, Reviews, Subscription, Trainer
from django.db.models import Sum


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Подписка на рассылку
    """
    class Meta:
        model = Subscription
        fields = ("email",)


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


class ReviewsSerializer(serializers.ModelSerializer):
    """
    Список отзывов
    """
    # rating = serializers.IntegerField(min_value=1, max_value=5)
    user = serializers.CharField(source="user.username", read_only=True)
    created_at = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M:%S", read_only=True)
    trainer = serializers.StringRelatedField(read_only=True)
    # trainer = serializers.StringRelatedField(source="trainer.first_name")

    class Meta:
        model = Reviews
        fields = "__all__"


class CreateReviewsSerializer(serializers.ModelSerializer):
    """
    Представление для создания отзывов
    """
    class Meta:
        model = Reviews
        fields = ("rating", "text", "trainer")


class TrainerListSerializer(serializers.ModelSerializer):
    """
    Список тренеров на домашней странице
    """
    class Meta:
        model = Trainer
        fields = ("id", "avatar")


class TrainerSerializer(serializers.ModelSerializer):
    """
    Детальная информация о тренере
    """
    trainer_reviews = ReviewsSerializer(many=True, read_only=True)
    position = serializers.CharField(source="get_position_display")
    count_reviews = serializers.SerializerMethodField()
    total_rating = serializers.SerializerMethodField()

    class Meta:
        model = Trainer
        fields = "__all__"

    def get_count_reviews(self, obj):
        return obj.trainer_reviews.count()

    def get_total_rating(self, obj):
        total_sum = obj.trainer_reviews.aggregate(
            Sum("rating"))["rating__sum"]
        print(type(total_sum))
        return total_sum / obj.trainer_reviews.count() if total_sum else 0
