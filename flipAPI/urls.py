from rest_framework.routers import DefaultRouter
from .views import FlashcardViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'flashcards', FlashcardViewSet, basename='flashcard')

urlpatterns = [
    # This will include all URLs that the router handles
    path('', include(router.urls)),
]
