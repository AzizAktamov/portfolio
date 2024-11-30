from django.contrib import admin
from .models import About,Portfolio,Contact

admin.site.register((About,Contact,Portfolio))

