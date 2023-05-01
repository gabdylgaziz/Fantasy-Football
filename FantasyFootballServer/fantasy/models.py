from django.db import models

# Create your models here.

class Team(models.Model):
    team_id = models.IntegerField() 
    team_name = models.CharField(max_length=40) 

class User(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    age = models.FloatField()
    gender = models.CharField(max_length=10)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    
class User_Squad(models.Model):
    user_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_team = models.JSONField(encoder=None)
    
class User_Score(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Player(models.Model):
    player_id = models.IntegerField()
    name = models.CharField(max_length=40)
    price = models.FloatField()
    strength = models.FloatField()
    role = models.CharField(max_length=40)

