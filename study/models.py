from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.team_name

class Students(models.Model):
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE,related_name="members", default=None)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    