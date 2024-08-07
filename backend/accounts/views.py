from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer

User = get_user_model()


@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        }
    )


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        refresh = RefreshToken.for_user(user)
        data["token"] = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)
