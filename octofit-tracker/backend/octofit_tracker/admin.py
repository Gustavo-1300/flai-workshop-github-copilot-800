from django.contrib import admin
from .models import Team, Activity, Leaderboard, Workout, UserProfile


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_type', 'user_id', 'duration', 'distance', 'calories', 'date']
    search_fields = ['activity_type', 'user_id']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['username', 'rank', 'total_activities', 'total_duration', 
                    'total_calories', 'total_distance', 'last_updated']
    search_fields = ['username']
    list_filter = ['rank', 'last_updated']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'duration', 'calories_estimate', 'created_at']
    search_fields = ['title', 'category']
    list_filter = ['category', 'difficulty', 'created_at']
    ordering = ['difficulty', 'duration']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'age', 'weight', 'height', 'fitness_goal', 'team_id']
    search_fields = ['username', 'email']
    list_filter = ['created_at', 'updated_at']
    ordering = ['username']
