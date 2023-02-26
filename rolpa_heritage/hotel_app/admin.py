from django.contrib import admin
from .models import *

admin.site.site_header = "Hotel Rolpa Heritage"
admin.site.site_title = "Hotel Rolpa Heritage"
admin.site.index_title = "Hotel Rolpa Heritage"

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Clients)
admin.site.register(Rating)
