from django.db import models

# Create your models here.
class addrawdata(models.Model):
    About=models.TextField()
    years_experience=models.IntegerField()
    project_deliverd=models.IntegerField()
    def __str__(self):
        return self.About
class addProjects(models.Model):
    identity=models.CharField(null=True,max_length=20)
    image=models.ImageField()
    title=models.CharField(max_length=100)
    description=models.TextField()
    link=models.URLField()
    def __str__(self):
        return self.title
