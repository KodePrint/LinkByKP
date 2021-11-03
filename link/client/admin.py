from django.contrib import admin
from client.models import Branch, Company

from import_export.admin import ImportExportModelAdmin

# Register your models here.

class BranchAdmin(ImportExportModelAdmin):
    
    class Meta:
        model = Branch

admin.site.register(Branch, BranchAdmin)
admin.site.register(Company)