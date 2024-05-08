from django.contrib import admin
from .models import company,job,registration

# Register your models here.
admin.site.register(company)
admin.site.register(job)

class registraionadmin(admin.ModelAdmin):
    list_display = ('id','c_name','c_phone','c_email','c_qualif','company_name')
admin.site.register(registration,registraionadmin)






