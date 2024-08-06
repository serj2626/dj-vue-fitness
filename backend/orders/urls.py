from django.urls import path
from .views import AbonemenListtView, OrderAbonementCreateView, OrderTrainingCreateView

urlpatterns = [
    path("abonements/", AbonemenListtView.as_view(), name="abonement-list"),
    path("abonements/<int:pk>/buy/", OrderAbonementCreateView.as_view(), name="abonement-buy"),
    path("trainers/<pk>/", OrderTrainingCreateView.as_view(), name="training-create"),
]