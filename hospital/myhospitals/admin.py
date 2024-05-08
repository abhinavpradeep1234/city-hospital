from django.contrib import admin
from .models import departments,doctors1,bookings,name
admin.site.register(departments)
admin.site.register(doctors1)
admin.site.register(name)
class bookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name' ,'p_phone' ,'p_email', 'doc_name','booking_date')
admin.site.register(bookings,bookingsAdmin)