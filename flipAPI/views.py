from django.shortcuts import render
from rest_framework import viewsets
from .models import Flashcard
from .serializers import FlashcardSerializer
import os
from django.http import Http404, HttpResponseServerError, HttpResponse
from django.utils._os import safe_join
from django.views.static import serve as static_serve
from pathlib import Path
import posixpath
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings

class CognitoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None
        try:
            # Assuming the token prefix is 'Bearer' followed by a space
            token = authorization_header.split(' ')[1]
            # Decode the JWT from the token
            decoded_token = jwt.decode(
                token, 
                settings.COGNITO_JWT_KEY, 
                algorithms=["RS256"], 
                audience=settings.COGNITO_AUDIENCE
            )
            # Example validation: check if the token has the correct issuer
            if decoded_token['iss'] != f'https://cognito-idp.{settings.COGNITO_REGION}.amazonaws.com/{settings.COGNITO_USER_POOL_ID}':
                raise AuthenticationFailed('Invalid token issuer.')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.PyJWTError as e:
            raise AuthenticationFailed(f'Error decoding token: {str(e)}')

        # Implement additional token validation logic if necessary
        # For example, you could query your database to check if the user exists

        # Return a user instance if valid (modify according to your user handling logic)
        return (request.user, None)

    def authenticate_header(self, request):
        return 'Bearer'

class FlashcardViewSet(viewsets.ModelViewSet):
    authentication_classes = [CognitoAuthentication]  # Apply CognitoAuthentication
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    
def home(request):
    return HttpResponse("Welcome to the home page!")
    
def serve_react(request, path='', document_root=None):
    if not document_root or not os.path.isdir(document_root):
        return HttpResponseServerError("Server configuration error.")

    path = posixpath.normpath(path).lstrip("/")
    fullpath = Path(safe_join(document_root, path))

    if fullpath.is_file():
        return static_serve(request, path, document_root=document_root)
    else:
        index_path = Path(safe_join(document_root, "index.html"))
        if not index_path.is_file():
            return Http404("index.html not found.")

        return static_serve(request, "index.html", document_root=document_root)
