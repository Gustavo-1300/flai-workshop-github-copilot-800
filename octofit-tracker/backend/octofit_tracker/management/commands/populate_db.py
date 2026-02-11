from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, Activity, Leaderboard, Workout, UserProfile
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()

        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! The mightiest heroes of Earth.',
            members=[1, 2, 3, 4, 5]
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League - protecting Earth from threats.',
            members=[6, 7, 8, 9, 10]
        )

        # Create User Profiles
        self.stdout.write('Creating user profiles...')
        marvel_heroes = [
            {'user_id': 1, 'username': 'ironman', 'email': 'tony.stark@avengers.com', 'age': 48, 'weight': 85, 'height': 185, 'fitness_goal': 'Maintain peak performance', 'team_id': str(team_marvel._id)},
            {'user_id': 2, 'username': 'captainamerica', 'email': 'steve.rogers@avengers.com', 'age': 105, 'weight': 95, 'height': 188, 'fitness_goal': 'Super soldier strength', 'team_id': str(team_marvel._id)},
            {'user_id': 3, 'username': 'thor', 'email': 'thor@asgard.com', 'age': 1500, 'weight': 110, 'height': 198, 'fitness_goal': 'Godly endurance', 'team_id': str(team_marvel._id)},
            {'user_id': 4, 'username': 'hulk', 'email': 'bruce.banner@avengers.com', 'age': 49, 'weight': 150, 'height': 244, 'fitness_goal': 'Control transformation', 'team_id': str(team_marvel._id)},
            {'user_id': 5, 'username': 'blackwidow', 'email': 'natasha.romanoff@avengers.com', 'age': 36, 'weight': 59, 'height': 170, 'fitness_goal': 'Agility and flexibility', 'team_id': str(team_marvel._id)},
        ]

        dc_heroes = [
            {'user_id': 6, 'username': 'superman', 'email': 'clark.kent@dailyplanet.com', 'age': 35, 'weight': 107, 'height': 191, 'fitness_goal': 'Maintain Kryptonian power', 'team_id': str(team_dc._id)},
            {'user_id': 7, 'username': 'batman', 'email': 'bruce.wayne@wayne.com', 'age': 42, 'weight': 95, 'height': 188, 'fitness_goal': 'Peak human condition', 'team_id': str(team_dc._id)},
            {'user_id': 8, 'username': 'wonderwoman', 'email': 'diana@themyscira.com', 'age': 800, 'weight': 75, 'height': 183, 'fitness_goal': 'Amazon warrior strength', 'team_id': str(team_dc._id)},
            {'user_id': 9, 'username': 'flash', 'email': 'barry.allen@starlabs.com', 'age': 29, 'weight': 81, 'height': 183, 'fitness_goal': 'Speed and stamina', 'team_id': str(team_dc._id)},
            {'user_id': 10, 'username': 'aquaman', 'email': 'arthur.curry@atlantis.com', 'age': 38, 'weight': 145, 'height': 193, 'fitness_goal': 'Underwater endurance', 'team_id': str(team_dc._id)},
        ]

        for hero_data in marvel_heroes + dc_heroes:
            UserProfile.objects.create(**hero_data)

        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['running', 'swimming', 'cycling', 'strength training', 'combat training', 'flying']
        
        for user_id in range(1, 11):
            for i in range(random.randint(8, 15)):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                distance = round(random.uniform(2, 50), 2) if activity_type in ['running', 'swimming', 'cycling', 'flying'] else None
                calories = duration * random.randint(5, 15)
                
                Activity.objects.create(
                    user_id=user_id,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    notes=f'{activity_type.capitalize()} session for superhero training'
                )

        # Create Leaderboard
        self.stdout.write('Creating leaderboard entries...')
        all_profiles = UserProfile.objects.all()
        leaderboard_data = []
        
        for profile in all_profiles:
            user_activities = Activity.objects.filter(user_id=profile.user_id)
            total_activities = user_activities.count()
            total_duration = sum(a.duration for a in user_activities)
            total_calories = sum(a.calories or 0 for a in user_activities)
            total_distance = sum(a.distance or 0 for a in user_activities)
            
            leaderboard_data.append({
                'user_id': profile.user_id,
                'username': profile.username,
                'total_activities': total_activities,
                'total_duration': total_duration,
                'total_calories': total_calories,
                'total_distance': round(total_distance, 2)
            })
        
        # Sort by total_calories and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_calories'], reverse=True)
        for rank, data in enumerate(leaderboard_data, start=1):
            Leaderboard.objects.create(
                rank=rank,
                **data
            )

        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts_data = [
            {
                'title': 'Super Soldier Training',
                'description': 'Captain America\'s legendary training routine for peak human performance',
                'category': 'strength',
                'difficulty': 'advanced',
                'duration': 90,
                'calories_estimate': 800,
                'exercises': ['Push-ups: 100 reps', 'Pull-ups: 50 reps', 'Shield throws: 30 reps', 'Combat drills: 20 min']
            },
            {
                'title': 'Asgardian Power Workout',
                'description': 'Thor\'s godly strength and endurance training',
                'category': 'strength',
                'difficulty': 'advanced',
                'duration': 120,
                'calories_estimate': 1000,
                'exercises': ['Hammer curls: 50 reps', 'Thunder squats: 100 reps', 'Lightning lifts: 30 reps', 'Battle meditation: 15 min']
            },
            {
                'title': 'Speed Force Cardio',
                'description': 'Flash\'s high-intensity speed training program',
                'category': 'cardio',
                'difficulty': 'intermediate',
                'duration': 45,
                'calories_estimate': 600,
                'exercises': ['Sprint intervals: 10x100m', 'Speed stairs: 15 min', 'Agility drills: 20 min']
            },
            {
                'title': 'Amazon Warrior Conditioning',
                'description': 'Wonder Woman\'s complete warrior fitness routine',
                'category': 'strength',
                'difficulty': 'advanced',
                'duration': 75,
                'calories_estimate': 750,
                'exercises': ['Lasso swings: 50 reps', 'Shield blocks: 100 reps', 'Sword forms: 30 min', 'Combat kata: 15 min']
            },
            {
                'title': 'Detective Agility Training',
                'description': 'Batman\'s stealth and agility workout',
                'category': 'flexibility',
                'difficulty': 'intermediate',
                'duration': 60,
                'calories_estimate': 500,
                'exercises': ['Parkour drills: 20 min', 'Grappling practice: 25 min', 'Stealth movements: 15 min']
            },
            {
                'title': 'Underwater Endurance',
                'description': 'Aquaman\'s swimming and underwater strength program',
                'category': 'cardio',
                'difficulty': 'intermediate',
                'duration': 60,
                'calories_estimate': 550,
                'exercises': ['Ocean swim: 5km', 'Deep diving: 30 min', 'Underwater combat: 20 min']
            },
            {
                'title': 'Arc Reactor Cardio',
                'description': 'Iron Man\'s high-tech cardio routine',
                'category': 'cardio',
                'difficulty': 'beginner',
                'duration': 30,
                'calories_estimate': 350,
                'exercises': ['Treadmill run: 3km', 'Cycling: 15 min', 'Cool-down walk: 10 min']
            },
            {
                'title': 'Kryptonian Strength',
                'description': 'Superman\'s legendary strength training',
                'category': 'strength',
                'difficulty': 'advanced',
                'duration': 90,
                'calories_estimate': 900,
                'exercises': ['Bench press: 200 reps', 'Deadlifts: 150 reps', 'Flight simulation: 30 min']
            },
            {
                'title': 'Spy Flexibility Routine',
                'description': 'Black Widow\'s flexibility and stealth training',
                'category': 'flexibility',
                'difficulty': 'beginner',
                'duration': 45,
                'calories_estimate': 300,
                'exercises': ['Dynamic stretching: 15 min', 'Yoga flow: 20 min', 'Balance drills: 10 min']
            },
            {
                'title': 'Gamma Strength Circuit',
                'description': 'Hulk\'s raw power training circuit',
                'category': 'strength',
                'difficulty': 'advanced',
                'duration': 60,
                'calories_estimate': 850,
                'exercises': ['Smash training: 100 reps', 'Power cleans: 75 reps', 'Rage meditation: 10 min']
            }
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'Teams created: {Team.objects.count()}')
        self.stdout.write(f'User profiles created: {UserProfile.objects.count()}')
        self.stdout.write(f'Activities created: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries created: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('='*50))
