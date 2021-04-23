from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from book_management.models import Book
from book_management.serializers import BookSerializer


class UpdateBookView(UpdateAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_url_kwarg = 'id'
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
