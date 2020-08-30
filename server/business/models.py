from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100, null=True)
    tags = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    # TODO: Define all the fields 

    def __str__(self):
        return self.name