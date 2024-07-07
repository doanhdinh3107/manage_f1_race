from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
class GrandBahrain(models.Model):
    date=models.DateTimeField(default=timezone.now)
    team=models.CharField(max_length=50,default="")
    point=models.IntegerField(default=0)
    def __str__(self):
            return self.team

class GrandAustralia(models.Model):
    date=models.DateTimeField(default=timezone.now)
    team=models.CharField(max_length=50,default="")
    point=models.IntegerField(default=0)
    def __str__(self):
            return self.team
class GrandJapan(models.Model):
    date=models.DateTimeField(default=timezone.now)
    team=models.CharField(max_length=50,default="")
    point=models.IntegerField(default=0)
    def __str__(self):
            return self.team
class Team(models.Model):
    name=models.CharField(max_length=100)
    point=models.IntegerField(default=0)
    logo =models.CharField(max_length=300)
    description=models.TextField()
    image=models.CharField(max_length=300)
    grandjapan = models.ForeignKey(GrandJapan, related_name="+", on_delete=models.PROTECT,default=1)
    grandaustralia = models.ForeignKey(GrandAustralia,related_name="+",  on_delete=models.PROTECT,default=1)
    grandbahrain = models.ForeignKey(GrandBahrain,related_name="+",on_delete=models.PROTECT,default=1)
    def __str__(self):
        return self.name
    class Meta:
        ordering=('-point',)
class Racer(models.Model):
     avatar=models.CharField(max_length=350)
     name=models.CharField( max_length=150)
     birth=models.DateTimeField(default=timezone.now)
     team=models.ForeignKey(Team,related_name="+",on_delete=models.PROTECT,default=1)
     bio=models.TextField(max_length=3000)
     point=models.IntegerField(default=0)
     def __str__(self):
          return self.name
     class Meta:
          ordering=('-point',)