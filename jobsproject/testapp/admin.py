from django.contrib import admin
from testapp.models import hydjobs
# Register your models here.
class hydjobsadmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','eligibility','address','email','phonenumber']
admin.site.register(hydjobs,hydjobsadmin)
