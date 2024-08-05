from .models import Trainer,  Reviews, Rate, Post
from .serializers import TrainerSerializer, RateSerializer, PostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    lookup_field = 'category'

class RateListView(ListAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()


class TrainerListView(ListAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()


class TrainerDetailView(RetrieveAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
