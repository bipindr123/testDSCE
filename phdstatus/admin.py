from django.contrib import admin

# Register your models here.
from .models import PhdStatus, WorkStatusTable, ComprehensiveTable, WorkshopsTable, TrainingTable, \
    FundedProjectsTable

admin.site.site_header = 'DSCE Research Management Administration'


class WorkStatusTableInline(admin.TabularInline):
    model = WorkStatusTable
    extra = 1

class ComprehensiveTableInline(admin.TabularInline):
    model = ComprehensiveTable
    extra = 1


class WorkshopsTableInline(admin.TabularInline):
    model = WorkshopsTable
    extra = 1



class TrainingTableInline(admin.TabularInline):
    model = TrainingTable
    extra = 1


class FundedProjectsTableInline(admin.TabularInline):
    model = FundedProjectsTable
    extra = 1


class PhdstatusAdmin(admin.ModelAdmin):
    radio_fields = {"synopsys": admin.HORIZONTAL}
    fields = (
        'name','status','synopsys', 'dept', 'guide', 'uni', 'year', 'other')

    inlines = [WorkStatusTableInline,ComprehensiveTableInline,WorkshopsTableInline,TrainingTableInline,FundedProjectsTableInline]

admin.site.register(PhdStatus, PhdstatusAdmin)
