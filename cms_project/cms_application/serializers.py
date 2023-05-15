from rest_framework import serializers
from .models import customer, Post, Like

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField(source='like_count')

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.like_count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
