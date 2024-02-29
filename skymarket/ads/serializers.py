from rest_framework import serializers
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'ad', 'created_at']


class AdSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['title', 'price', 'description', 'author', 'created_at', 'comments']


class AdDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['title', 'price', 'description', 'author', 'created_at', 'comments']
