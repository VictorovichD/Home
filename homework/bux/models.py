from django.db import models
class Project(models.Model):
    image = models.ImageField(upload_to='img/')

class Guys(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name