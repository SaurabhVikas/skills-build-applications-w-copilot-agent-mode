from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team='Marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC'),
            User.objects.create(email='superman@dc.com', name='Superman', team='DC'),
        ]

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30)
        Activity.objects.create(user='Captain America', activity_type='Cycling', duration=45)
        Activity.objects.create(user='Batman', activity_type='Swimming', duration=60)
        Activity.objects.create(user='Superman', activity_type='Flying', duration=120)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=90)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard')
        Workout.objects.create(name='Agility Boost', description='Agility and speed drills', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
