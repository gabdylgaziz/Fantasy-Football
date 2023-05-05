from rest_framework import serializers 
from .models import *
from account.serializers import UserSerializer
        
class TeamSerializer(serializers.Serializer):
    team_id = serializers.IntegerField() 
    team_name = serializers.CharField(max_length=40) 
    
    def create(self, validated_data):
        return TeamSerializer.objects.create(**validated_data)
        
class UserSquadSerializer(serializers.Serializer):
    user_id = UserSerializer()
    user_team = serializers.CharField(max_length=150)
    
    def create(self, validated_data):
        return UserSquadSerializer.objects.create(**validated_data)
    
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'surname',
                  'email',
                  'age',
                  'gender',
                  'team_id'
                  )
        
class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('team_id',
                  'team_name'
                  )
        
class UserSquadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Squad
        fields = ('user_id',
                  'user_name'
                )
        
class UserScoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Score
        fields = ('user_id',
                  'score'
                )

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"

class FootballerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = "__all__"