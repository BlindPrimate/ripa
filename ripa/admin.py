from django.contrib import admin
from .models import Defect, Project, Release, RFC, Feature

# Register your models here.

admin.site.register(Defect)
admin.site.register(Project)
admin.site.register(Release)
admin.site.register(RFC)
admin.site.register(Feature)
