from django.contrib import admin

# Register your models here.
from listings.models import Band
from listings.models import Listing


admin.site.register(Band)
admin.site.register(Listing)