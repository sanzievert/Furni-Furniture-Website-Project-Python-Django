from django.contrib import admin
from Habibapp.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    clist=['Firstname','Lastname','Email','message']
admin.site.register(Contact,ContactAdmin)
