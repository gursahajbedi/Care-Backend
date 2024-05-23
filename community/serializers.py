from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='User')
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.total_likes()

    def get_dislikes_count(self, obj):
        return obj.total_dislikes()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'parent', 'created_at',
                    'likes_count', 'dislikes_count')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')  # Adjust as necessary
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.total_likes()

    def get_dislikes_count(self, obj):
        return obj.total_dislikes()

    def get_comments(self, obj):
        top_level_comments = obj.comments.filter(parent=None)
        return NestedCommentSerializer(top_level_comments, many=True).data

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'desc', 'published_date',
                  'likes_count', 'dislikes_count', 'comments')
        

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class NestedCommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.total_likes()

    def get_dislikes_count(self, obj):
        return obj.total_dislikes()

    def get_replies(self, obj):
        # Recursively serialize replies
        replies = obj.replies.all()
        return NestedCommentSerializer(replies, many=True).data

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'parent', 'created_at',
                  'likes_count', 'dislikes_count', 'replies')