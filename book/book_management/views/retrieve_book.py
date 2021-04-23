from rest_framework.generics import RetrieveAPIView

from book_management.models import Book
from book_management.serializers import RetrieveBookSerializer


class BookRetrieveView(RetrieveAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = RetrieveBookSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['id'])
