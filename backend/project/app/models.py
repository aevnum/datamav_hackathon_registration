from django.db import models

# Create your models here.

class Problem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=255)
    college = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
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