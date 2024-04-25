
from rest_framework import serializers
from .models import Title, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'front', 'back']

class TitleSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'title', 'cards']




#OLD SERIALIZERS.PY
# # myapp/serializers.py
# from rest_framework import serializers
# from .models import Flashcard, Flashcard_Set, User, User_Flashcard_Set, Study_Session

# class FlashcardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Flashcard
#         fields = '__all__'

# class FlashcardSetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Flashcard_Set
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class UserFlashcardSetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User_Flashcard_Set
#         fields = '__all__'

# class StudySessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Study_Session
#         fields = '__all__'
