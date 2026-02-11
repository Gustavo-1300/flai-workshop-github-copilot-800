from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Team, Activity, Leaderboard, Workout, UserProfile
from .serializers import (
    TeamSerializer, ActivitySerializer, LeaderboardSerializer,
    WorkoutSerializer, UserProfileSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint that provides links to all available endpoints.
    """
    return Response({
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'user-profiles': reverse('userprofile-list', request=request, format=format),
    })


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing teams.
    Provides CRUD operations for teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing activities.
    Provides CRUD operations for user activities.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    def get_queryset(self):
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing leaderboard entries.
    Provides CRUD operations and ranking functionality.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing workout suggestions.
    Provides CRUD operations for workout plans.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
    def get_queryset(self):
        queryset = Workout.objects.all()
        difficulty = self.request.query_params.get('difficulty', None)
        category = self.request.query_params.get('category', None)
        
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        if category is not None:
            queryset = queryset.filter(category=category)
        
        return queryset


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user profiles.
    Provides CRUD operations for user profile data.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        queryset = UserProfile.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
