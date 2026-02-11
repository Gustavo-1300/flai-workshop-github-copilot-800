from djongo import models
from django.contrib.auth.models import User


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.JSONField(default=list)  # List of user IDs
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.IntegerField()
    activity_type = models.CharField(max_length=100)  # running, cycling, swimming, etc.
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(blank=True, null=True)  # in kilometers
    calories = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.activity_type} - {self.duration}min"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.IntegerField()
    username = models.CharField(max_length=150)
    total_activities = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # in minutes
    total_calories = models.IntegerField(default=0)
    total_distance = models.FloatField(default=0.0)  # in kilometers
    rank = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']
    
    def __str__(self):
        return f"{self.username} - Rank {self.rank}"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)  # strength, cardio, flexibility, etc.
    difficulty = models.CharField(max_length=50)  # beginner, intermediate, advanced
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    exercises = models.JSONField(default=list)  # List of exercises with sets/reps
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
        ordering = ['difficulty', 'duration']
    
    def __str__(self):
        return f"{self.title} ({self.difficulty})"


class UserProfile(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)  # in kg
    height = models.FloatField(blank=True, null=True)  # in cm
    fitness_goal = models.CharField(max_length=200, blank=True)
    team_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_profiles'
    
    def __str__(self):
        return self.username
