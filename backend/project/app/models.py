from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Problem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    img = models.TextField(default='https://hotpot.ai/images/site/ai/restorer/teaser_400.jpg')
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True)
    college = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.username
    

class Teams(models.Model):
    name = models.CharField(max_length=100, unique=True)
    team_id = models.CharField(max_length=10, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    members = models.ManyToManyField(User, related_name='teams')
    
    def __str__(self):
        return self.name

class Submission(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Submission by {self.team} for {self.problem}'