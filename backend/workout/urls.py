from django.urls import path
from .views import RateListView, TrainerListView, TrainerDetailView

urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainer-list"),
    path("trainers/<pk>/", TrainerDetailView.as_view(), name="trainer-detail"),
    path("rates/", RateListView.as_view(), name="rate-list"),
]
