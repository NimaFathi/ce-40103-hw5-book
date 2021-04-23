from rest_framework.generics import DestroyAPIView

from book_management.models import Book
from book_management.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class DeleteBookView(DestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    model = Book
    serializer_class = BookSerializer

    def get_queryset(self):
        return self.model.objects.order_by('-id')

    def perform_destroy(self, instance):
        instance.delete()
