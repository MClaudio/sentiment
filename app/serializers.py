from app import models
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Movie

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Comment