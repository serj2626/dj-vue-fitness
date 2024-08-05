from django.urls import path
from .views import (RateListView, TrainerListView, TrainerDetailView,
                    PostListView, PostDetailView,
                    ReviewsDetailView, ReviewsListView, SubscriptionView)

urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainer-list"),
    path("trainers/<pk>/", TrainerDetailView.as_view(), name="trainer-detail"),
    path("rates/", RateListView.as_view(), name="rate-list"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<str:category>/", PostDetailView.as_view(), name="post-detail"),
    path("subscribe/", SubscriptionView.as_view(), name="subscribe"),
    path("reviews/", ReviewsListView.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewsDetailView.as_view(), name="review-detail"),
]
