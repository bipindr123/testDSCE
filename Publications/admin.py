from django.contrib import admin
from django.utils.translation import ugettext_lazy

from .models import publication


# Register your models here.
admin.site.site_header = 'DSCE Research Management Administration'

class publicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dept', 'year')
    search_fields = ('title', 'author')
    list_filter = ('year',)


admin.site.register(publication, publicationAdmin)
