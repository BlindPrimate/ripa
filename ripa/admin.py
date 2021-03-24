from django.contrib import admin
from .models import Defect, Project, Release

# Register your models here.

admin.site.register(Defect)
admin.site.register(Project)
admin.site.register(Release)
