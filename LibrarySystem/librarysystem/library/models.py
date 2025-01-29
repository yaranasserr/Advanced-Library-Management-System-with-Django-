from django.db import models
from geopy.distance import geodesic
from users.models import Profile

class Library(models.Model):
    library_name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    latitude = models.FloatField() 
    longitude = models.FloatField()  

    def __str__(self):
        return self.library_name
    
    def get_distance_from_user(self, user_lat, user_lon):
        library_location = (self.latitude, self.longitude)
        user_location = (user_lat, user_lon)
        if user_lat and user_lon:
            return round(geodesic(library_location, user_location).kilometers, 2)
        return None 


