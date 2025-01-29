# models.py
from django.db import models
from django.contrib.auth.models import User
from geopy.geocoders import Nominatim

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def update_location(self):
        
        full_address = f"{self.street_address}, {self.city}, {self.state_province}, {self.postal_code}, {self.country}"

        geolocator = Nominatim(user_agent="library_system")
        location = geolocator.geocode(full_address)

        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude
            self.save()  # Save the updated latitude and longitude to the database
        else:
            # Optionally, log an error or handle the case where no location is found
            self.latitude = None
            self.longitude = None
            self.save()
    
