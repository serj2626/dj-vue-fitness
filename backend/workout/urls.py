from django.urls import path

from .views import (
    PostDetailView,
    PostListView,
    RateListView,
    ReviewsDetailView,
    SubscriptionView,
    TrainerDetailView,
    TrainerListForPageView,
    TrainerListView,
    CreateReviewsView
)

urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainer-list"),
    path("all-trainers/", TrainerListForPageView.as_view(), name="all-trainer-list"),
    path("trainers/<pk>/", TrainerDetailView.as_view(), name="trainer-detail"),
    path("rates/", RateListView.as_view(), name="rate-list"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<str:category>/", PostDetailView.as_view(), name="post-detail"),
    path("subscribe/", SubscriptionView.as_view(), name="subscribe"),
    path("reviews/create", CreateReviewsView.as_view(), name="review-create"),
    path("reviews/<int:pk>/", ReviewsDetailView.as_view(), name="review-detail"),
]
