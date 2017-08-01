from django.contrib import admin
from projects.models import Project


# Register your models here.
admin.site.site_header = 'DSCE Research Management Administration'
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
