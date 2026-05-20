from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User.objects.create(email='captain@marvel.com', username='Captain America', team=marvel),
            User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User.objects.create(email='batman@dc.com', username='Batman', team=dc),
            User.objects.create(email='superman@dc.com', username='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='swim', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='run', duration=40, date=timezone.now().date())
        Activity.objects.create(user=users[4], activity_type='cycle', duration=35, date=timezone.now().date())
        Activity.objects.create(user=users[5], activity_type='swim', duration=50, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Situps', description='Core strength')
        w3 = Workout.objects.create(name='Sprints', description='Speed training')
        w1.suggested_for.set([users[0], users[3]])
        w2.suggested_for.set([users[1], users[4]])
        w3.suggested_for.set([users[2], users[5]])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, score=100)
        Leaderboard.objects.create(team=dc, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
