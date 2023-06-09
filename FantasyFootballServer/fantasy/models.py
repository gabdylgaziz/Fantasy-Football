from django.db import models
from account.models import UserData

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

    
class User_Score(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Club(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Footballer(models.Model):
    pos = {
        0 : 'GK',
        1 : 'DF',
        2 : 'MD',
        3 : 'FD'
    }
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    position = models.IntegerField(blank=True, choices=[
        (0, 'Goalkeeper'),
        (1, 'Defender'),
        (2, 'Midfielder'),
        (3, 'Forward'),
    ])
    jersy_number = models.IntegerField(blank=True)
    market_value = models.FloatField(blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.nick_name + ' ' + self.pos[self.position]


class User_Squad(models.Model):
    user_id = models.ForeignKey(UserData, on_delete=models.CASCADE)
    user_team = models.TextField()
