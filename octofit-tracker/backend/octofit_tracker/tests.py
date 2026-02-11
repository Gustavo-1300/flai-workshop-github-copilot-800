from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Team, Activity, Leaderboard, Workout, UserProfile


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team",
            members=[1, 2, 3]
        )
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(len(self.team.members), 3)
    
    def test_team_str(self):
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id=1,
            activity_type="running",
            duration=30,
            distance=5.0,
            calories=300
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, "running")
        self.assertEqual(self.activity.duration, 30)
    
    def test_activity_str(self):
        self.assertEqual(str(self.activity), "running - 30min")


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_id=1,
            username="testuser",
            total_activities=10,
            total_duration=300,
            total_calories=2000,
            total_distance=50.0,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        self.assertEqual(self.entry.username, "testuser")
        self.assertEqual(self.entry.rank, 1)
    
    def test_leaderboard_str(self):
        self.assertEqual(str(self.entry), "testuser - Rank 1")


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            title="Morning Run",
            description="A refreshing morning run",
            category="cardio",
            difficulty="beginner",
            duration=30,
            calories_estimate=300,
            exercises=["running", "stretching"]
        )
    
    def test_workout_creation(self):
        self.assertEqual(self.workout.title, "Morning Run")
        self.assertEqual(self.workout.difficulty, "beginner")
    
    def test_workout_str(self):
        self.assertEqual(str(self.workout), "Morning Run (beginner)")


class UserProfileModelTest(TestCase):
    """Test cases for UserProfile model"""
    
    def setUp(self):
        self.profile = UserProfile.objects.create(
            user_id=1,
            username="testuser",
            email="test@example.com",
            age=25,
            weight=70.0,
            height=175.0,
            fitness_goal="Get fit"
        )
    
    def test_profile_creation(self):
        self.assertEqual(self.profile.username, "testuser")
        self.assertEqual(self.profile.age, 25)
    
    def test_profile_str(self):
        self.assertEqual(str(self.profile), "testuser")


class APIEndpointTest(APITestCase):
    """Test cases for API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
    
    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('user-profiles', response.data)
    
    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_profiles_endpoint(self):
        response = self.client.get('/api/user-profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
