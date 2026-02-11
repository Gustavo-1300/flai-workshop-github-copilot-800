from rest_framework import serializers
from .models import Team, Activity, Leaderboard, Workout, UserProfile


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'distance', 
                  'calories', 'date', 'notes']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'username', 'total_activities', 'total_duration',
                  'total_calories', 'total_distance', 'rank', 'last_updated']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'category', 'difficulty', 
                  'duration', 'calories_estimate', 'exercises', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user_id', 'username', 'email', 'age', 'weight', 
                  'height', 'fitness_goal', 'team_id', 'created_at', 'updated_at']
    
    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None
