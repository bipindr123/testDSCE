from django.contrib import admin
from projects.models import FundedProject,Proposal


# Register your models here.
admin.site.site_header = 'DSCE Research Management Administration'
class FundedProjectAdmin(admin.ModelAdmin):
    pass

class ProposalAdmin(admin.ModelAdmin):
    pass

admin.site.register(FundedProject, FundedProjectAdmin)
admin.site.register(Proposal, ProposalAdmin)
