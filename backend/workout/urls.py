from django.urls import path
from .views import (RateListView, TrainerListView, TrainerDetailView,
                    PostListView, PostDetailView)

urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainer-list"),
    path("trainers/<pk>/", TrainerDetailView.as_view(), name="trainer-detail"),
    path("rates/", RateListView.as_view(), name="rate-list"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<str:category>/", PostDetailView.as_view(), name="post-detail"),
]
