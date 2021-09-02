from rest_framework import generics, mixins, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ValidationError

from courts.models import Court, Review
from .pagination import SmallSetPagination
from .serializers import CourtSerializer, ReviewSerializer
from .permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly


class CourtListCreateApiView(generics.ListCreateAPIView):
    queryset = Court.objects.all().order_by("-id")
    serializer_class = CourtSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


#  update(patch) delete:
class CourtEditApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateApiView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        court_pk = self.kwargs.get("pk")
        court = get_object_or_404(Court, pk=court_pk)
        review_author = self.request.user

        # if this user already made a review:
        review_queryset = Review.objects.filter(court=court,
                                                review_author=review_author)
        if review_queryset.exists():
            return
            raise ValidationError('You already made a review')

        serializer.save(court=court, review_author=review_author)


class ReviewEditApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = []





