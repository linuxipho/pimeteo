from django.contrib import admin
from pimeteo.models import Mesure, Live


class MesureAdmin(admin.ModelAdmin):
    list_display = ('time', 'temp', 'press', 'moist', 'dew')
    
class LiveAdmin(admin.ModelAdmin):
    list_display = ('time', 'temp', 'press', 'moist', 'dew')
    
admin.site.register(Mesure, MesureAdmin) 
admin.site.register(Live, LiveAdmin)