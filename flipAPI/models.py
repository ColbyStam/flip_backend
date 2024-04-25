from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    #password = models.CharField(max_length=200)  # handled by Cognito
    cognito_user_id = models.CharField(max_length=150, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

class Flashcard_Set(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

class Flashcard(models.Model):
    set = models.ForeignKey(Flashcard_Set, on_delete=models.CASCADE)
    front_text = models.TextField()
    back_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class User_Flashcard_Set(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    set = models.ForeignKey(Flashcard_Set, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    last_studied = models.DateTimeField(null=True, blank=True)

class Study_Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    set = models.ForeignKey(Flashcard_Set, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    score = models.IntegerField()