from django.contrib import admin
from prac.models import Jjal

# Register your models here.

class JjalAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Title', {'fields': ['jjal_text']}),
    ('Count', {'fields': ['cnt']}),
    #('Date information', {'fields': ['pub_date']}),
    ('File', {'fields': ['files']}),
  ]
  
admin.site.register(Jjal, JjalAdmin)