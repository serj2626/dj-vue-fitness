from rest_framework.generics import ListAPIView
from .serializers import AbonementSerializer
from .models import Abonement

class AbonemenListtView(ListAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer
