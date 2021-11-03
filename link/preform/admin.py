from django.contrib import admin
from preform.models import Preform, DetailPreform

# Register your models here.

class PreformAdmin(admin.ModelAdmin):
    list_display = ('generateIdentifier', 'date', 'total_cost', 'status')

admin.site.register(Preform, PreformAdmin)
admin.site.register(DetailPreform)
