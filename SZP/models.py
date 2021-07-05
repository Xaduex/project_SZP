from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    vacations_start = models.DateField(null=True)
    vacations_end = models.DateField(null=True)
    sick_leave = models.BooleanField(default=False)



#class Tweet(models.Model):
#    text = models.TextField()
#    owner = models.ForeignKey(User, on_delete=models.CASCADE)
#    creation_date = models.DateTimeField(auto_now_add=True)
#    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)