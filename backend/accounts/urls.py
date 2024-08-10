from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, get_my_info, MyAbonementListView, MytrainingListView

urlpatterns = [
    path("me/", get_my_info, name="my-info"),
    path("my-abonements/", MyAbonementListView.as_view(), name="my-abonements"),
    path("my-trainings/", MytrainingListView.as_view(), name="my-trainings"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
