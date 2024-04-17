from django.db import models

# Create your models here.
class FlashCard(models.Model):
    
    flashcard_id = models.AutoField()
    set_id = models.AutoField()
    front_text = models.TextField()
    back_text = models.TextField()
    created_at = models.DateTimeField()
    
    
    
class Flashcard_Set(models.Model):
    
    set_id = models.AutoField()
    user_id = models.AutoField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField()
    is_public = models.BooleanField()
    
    
    
class User(models.Model):
    
    user_id = models.AutoField()
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    last_login = models.DateTimeField()
 
 
 
class User_Flashcard_Set(models.Model):
    
    user_id = models.ForeignKey(to=User, on_delete=True)
    set_id = models.ForeignKey(to=Flashcard_Set, on_delete=True)
    is_favorite = models.BooleanField()
    last_studied = models.DateTimeField()
    
    
    
class Study_Session(models.Model):
    
    session_id = models.AutoField()
    user_id = models.ForeignKey(to=User, on_delete=True)
    set_id = models.ForeignKey(to=Flashcard_Set, on_delete=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    score = models.AutoField()
