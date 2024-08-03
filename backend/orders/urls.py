from django.urls import path
from .views import AbonemenListtView

urlpatterns = [
    path("abonemens/", AbonemenListtView.as_view(), name="abonemen-list"),
]