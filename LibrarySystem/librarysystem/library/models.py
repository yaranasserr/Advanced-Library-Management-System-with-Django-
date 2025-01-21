from django.db import models

class Library(models.Model):
    library_name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    latitude = models.FloatField() 
    longitude = models.FloatField()  

    def __str__(self):
        return self.library_name


