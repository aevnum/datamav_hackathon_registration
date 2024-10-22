from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Problem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True)
    college = models.CharField(max_length=255, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name='user permissions'
    )
    
    def __str__(self):
        return self.username
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Submission(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Submission by {self.team} for {self.problem}'