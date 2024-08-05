from .models import Trainer,  Reviews, Rate, Post, Subscription
from .serializers import (TrainerSerializer, RateSerializer, PostSerializer,
                          SubscriptionSerializer, ReviewsSerializer)
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView,
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView)


class ReviewsListView(ListCreateAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()


class ReviewsDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()

    # lookup_field = 'user'

    # def get_queryset(self):
    #     return Reviews.objects.filter(user=self.kwargs['pk'])

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['user'] = self.kwargs['pk']
    #     return context

    # def get_object(self):
    #     return Reviews.objects.get(user=self.kwargs['pk'])


class SubscriptionView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


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
