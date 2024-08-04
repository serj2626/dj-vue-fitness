from .models import Trainer, RatingTrainer, Reviews, Rate
from .serializers import TrainerSerializer, RateSerializer
from rest_framework.generics import ListAPIView


class RateListView(ListAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()


class TrainerListView(ListAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
