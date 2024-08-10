from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Post, Rate, Reviews, Subscription, Trainer


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("email",)


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "category",
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    # rating = serializers.IntegerField(min_value=1, max_value=5)
    user = serializers.CharField(source="user.username", read_only=True)
    created_at = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M:%S", read_only=True)
    trainer = serializers.StringRelatedField(read_only=True)
    # trainer = serializers.StringRelatedField(source="trainer.first_name")

    class Meta:
        model = Reviews
        fields = "__all__"


# class CreateReviewsSerializer(serializers.ModelSerializer):
#     rating = serializers.IntegerField(min_value=1, max_value=5)

#     class Meta:
#         model = Reviews
#         fields = ("rating", "text")


class TrainerSerializer(serializers.ModelSerializer):
    trainer_reviews = ReviewsSerializer(many=True, read_only=True)
    position = serializers.CharField(source="get_position_display")

    class Meta:
        model = Trainer
        fields = "__all__"
        include = ["trainer_reviews"]
