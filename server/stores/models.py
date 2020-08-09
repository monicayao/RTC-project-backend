from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stores(models.Model):
    name = models.CharField(max_length=100)
    # TODO: Define all the fields 

    def __str__(self):
        return self.name