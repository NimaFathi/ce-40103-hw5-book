import base64
from django.core.exceptions import ValidationError

from django.contrib.auth.hashers import make_password
from django.core.files import File
from rest_framework import serializers
from django.db import transaction

from book_management.models import Book


class RetrieveBookSerializer(serializers.ModelSerializer):
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
