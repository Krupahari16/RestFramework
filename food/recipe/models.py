from django.db import models

class Items(models.Model):

    food_name = models.CharField(max_length=200,null=True)

    food_type = models.CharField(max_length=200,null=True)

    description=models.TextField()

    ingredients=models.TextField()

    method=models.TextField()

    Category=models.TextField()


    def __str__(self):

        return self.food_name




