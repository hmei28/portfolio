from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Formation)
admin.site.register(PersoInformation)