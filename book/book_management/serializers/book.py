from rest_framework import serializers

from book_management.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'category', 'author_name', 'price')

    def validate(self, attrs):
        title = attrs.get('title', None)
        author = attrs.get('author_name', None)
        if title is None:
            raise serializers.ValidationError('title could not be empty')
        if author is None:
            raise serializers.ValidationError('category could not be empty')
        return attrs
