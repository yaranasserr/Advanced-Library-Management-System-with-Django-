from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'city', 'state_province', 'postal_code', 'country', 'latitude', 'longitude')

admin.site.register(Profile, ProfileAdmin)
