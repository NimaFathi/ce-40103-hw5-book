from rest_framework.generics import CreateAPIView

from book_management.serializers import BookSerializer


class CreateBookView(CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = BookSerializer
