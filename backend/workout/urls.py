from django.urls import path
from .views import RateListView, TrainerListView

urlpatterns = [
    path("trainers/", TrainerListView.as_view(), name="trainer-list"),
    # path("trainer/<int:pk>/", views.TrainerRetrieveUpdateDestroyAPIView.as_view()),
    path("rates/", RateListView.as_view(), name="rate-list"),
]