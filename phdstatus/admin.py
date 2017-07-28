from django.contrib import admin

# Register your models here.
from .models import PhdStatus, WorkDetailsTable, ComprehensiveTable, WorkshopsTable, PublicationsTable, TrainingTable, \
    FundedProjectsTable

admin.site.site_header = 'DSCE Research Management Administration'


class WorkDetailsInline(admin.TabularInline):
    model = WorkDetailsTable
    extra = 1

class ComprehensiveTableInline(admin.TabularInline):
    model = ComprehensiveTable
    extra = 1


class WorkshopsTableInline(admin.TabularInline):
    model = WorkshopsTable
    extra = 1


class PublicationsTableInline(admin.TabularInline):
    model = PublicationsTable
    extra = 1


class TrainingTableInline(admin.TabularInline):
    model = TrainingTable
    extra = 1


class FundedProjectsTableInline(admin.TabularInline):
    model = FundedProjectsTable
    extra = 1


class PhdstatusAdmin(admin.ModelAdmin):
    fields = (
        'name', 'dept', 'guide', 'uni', 'year', 'other')

    inlines = [WorkDetailsInline,ComprehensiveTableInline,PublicationsTableInline,WorkshopsTableInline,TrainingTableInline,FundedProjectsTableInline]

admin.site.register(PhdStatus, PhdstatusAdmin)
