from rest_framework import serializers

from .models import Post, Rate, Reviews, Subscription, Trainer


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("email",)


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "category",)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    created_at = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M:%S", read_only=True)
    trainer = serializers.StringRelatedField(source="trainer.first_name")

    class Meta:
        model = Reviews
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    trainer_reviews = ReviewsSerializer(many=True, read_only=True)
    position = serializers.CharField(source="get_position_display")

    class Meta:
        model = Trainer
        fields = "__all__"
        include = ["trainer_reviews"]
