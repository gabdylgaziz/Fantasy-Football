from rest_framework import serializers 
from .models import *
        
class TeamSerializer(serializers.Serializer):
    team_id = serializers.IntegerField() 
    team_name = serializers.CharField(max_length=40) 
    
    def create(self, validated_data):
        return TeamSerializer.objects.create(**validated_data)
    
class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    surname = serializers.CharField(max_length=40)
    email = serializers.CharField(max_length=40)
    age = serializers.FloatField()
    gender = serializers.CharField(max_length=10)
    team_id = TeamSerializer()
    
    def create(self, validated_data):
        return UserSerializer.objects.create(**validated_data)
        
class UserSquadSerializer(serializers.Serializer):
    user_id = TeamSerializer()
    user_team = serializers.JSONField(encoder=None)
    
    def create(self, validated_data):
        return UserSquadSerializer.objects.create(**validated_data)
        
class UserScoreSerializer(serializers.Serializer):
    user_id = UserSerializer()
    score = serializers.IntegerField()
    
    def create(self, validated_data):
        return UserScoreSerializer.objects.create(**validated_data)

    id = serializers.IntegerField()
    player_id = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    price = serializers.FloatField()
    strength = serializers.FloatField()
    role = serializers.CharField(max_length=40)
    
    def create(self, validated_data):
        return PlayerSerializer.objects.create(**validated_data)

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