"""
URL configuration for djangoFlip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from flipAPI.views import TitleViewSet, home, serve_react
#from flipAPI.views import FlashcardViewSet, home, serve_react
from django.conf import settings




router = DefaultRouter()
router.register(r'flashcards', TitleViewSet, basename='flashcards')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('', home, name='home'),
    # This regex matches any path that does NOT start with /api
    re_path(r'^(?!api/|admin/).*$', serve_react, {"document_root": settings.REACT_APP_BUILD_PATH}),
]

