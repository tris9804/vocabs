from rest_framework import serializers

from .models import User, Notebook, Vocabulary, Star

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = '__all__'

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'