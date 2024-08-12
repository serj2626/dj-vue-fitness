from django.urls import path

from .views import AbonemenListtView, OrderAbonementCreateView, OrderTrainingCreateView

urlpatterns = [
    path("abonements/", AbonemenListtView.as_view(), name="abonement-list"),
    path(
        "abonements/<int:pk>/order/",
        OrderAbonementCreateView.as_view(),
        name="abonement-buy",
    ),
    path(
        "trainings/create/order/",
        OrderTrainingCreateView.as_view(),
        name="training-create",)
]
